"""Class for dealing with HAP TLV data."""


class TLV:
    """This data is taken from Appendix 12 on page 251."""

    # Steps
    M1 = bytearray(b'\x01')
    M2 = bytearray(b'\x02')
    M3 = bytearray(b'\x03')
    M4 = bytearray(b'\x04')
    M5 = bytearray(b'\x05')
    M6 = bytearray(b'\x06')

    # Methods (see table 4-4 page 60)
    PairSetup = bytearray(b'\x01')
    PairVerify = bytearray(b'\x02')
    AddPairing = bytearray(b'\x03')
    RemovePairing = bytearray(b'\x04')
    ListPairings = bytearray(b'\x05')

    # TLV Values (see table 4-6 page 61)
    kTLVType_Method = 0
    kTLVType_Identifier = 1
    kTLVType_Salt = 2
    kTLVType_PublicKey = 3
    kTLVType_Proof = 4
    kTLVType_EncryptedData = 5
    kTLVType_State = 6
    kTLVType_Error = 7
    kTLVType_RetryDelay = 8
    kTLVType_Certificate = 9
    kTLVType_Signature = 10
    kTLVType_Permissions = 11  # 0x00 => reg. user, 0x01 => admin
    kTLVType_FragmentData = 12
    kTLVType_FragmentLast = 13
    kTLVType_Separator = 255

    # Errors (see table 4-5 page 60)
    kTLVError_Unknown = bytearray(b'\x01')
    kTLVError_Authentication = bytearray(b'\x02')
    kTLVError_Backoff = bytearray(b'\x03')
    kTLVError_MaxPeers = bytearray(b'\x04')
    kTLVError_MaxTries = bytearray(b'\x05')
    kTLVError_Unavailable = bytearray(b'\x06')
    kTLVError_Busy = bytearray(b'\x07')

    @staticmethod
    def decode_bytes(bs) -> dict:
        """
        Decode a byte string.

        :param bs: the byte string to decode
        :return: decoded TLV as a dict
        """
        return TLV.decode_bytearray(bytearray(bs))

    @staticmethod
    def decode_bytearray(ba: bytearray) -> dict:
        """
        Decode a bytearray.

        :param ba: the bytearray to decode
        :return: decoded TLV as a dict
        """
        result = {}

        # do not influence caller!
        tail = ba.copy()
        while len(tail) > 0:
            key = tail.pop(0)
            length = tail.pop(0)
            value = tail[:length]
            tail = tail[length:]

            if key not in result:
                result[key] = value
            else:
                for b in value:
                    result[key].append(b)

        return result

    @staticmethod
    def validate_tag(t: int) -> bool:
        """
        Validate a TLV tag.

        :param t: tag to validate
        :return: True if validation succeeded, False if not
        """
        try:
            val = int(t)
            if val < 0 or val > 255:
                valid = False
            else:
                valid = True
        except ValueError:
            valid = False
        return valid

    @staticmethod
    def encode_dict(d: dict) -> bytearray:
        """
        Encode a dict as a TLV bytearray.

        :param d: dict to encode
        :returns: bytearray containing encoded dict
        :raises ValueError: if dict failed to encode
        """
        result = bytearray()
        for key in d:
            if not TLV.validate_tag(key):
                raise ValueError('Invalid tag')

            value = d[key]

            # handle separators properly
            if key == TLV.kTLVType_Separator:
                if len(value) == 0:
                    result.append(key)
                    result.append(0)
                else:
                    raise ValueError('Separator must not have data')

            while len(value) > 0:
                result.append(key)
                if len(value) > 255:
                    length = 255
                    result.append(length)
                    for b in value[:length]:
                        result.append(b)
                    value = value[length:]
                else:
                    length = len(value)
                    result.append(length)
                    for b in value[:length]:
                        result.append(b)
                    value = value[length:]

        return result
