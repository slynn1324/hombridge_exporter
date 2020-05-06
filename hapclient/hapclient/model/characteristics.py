"""Accessory characteristic types."""


class _CharacteristicTypes(object):
    """This data is taken from Apple-defined Characteristics on page 144."""

    ACCESSORY_PROPERTIES = 'A6'
    ACTIVE = 'B0'
    ADMINISTRATOR_ONLY_ACCESS = '1'
    AIR_PARTICULATE_DENSITY = '64'
    AIR_PARTICULATE_SIZE = '65'
    AIR_PURIFIER_STATE_CURRENT = 'A9'
    AIR_PURIFIER_STATE_TARGET = 'A8'
    AIR_QUALITY = '95'
    AUDIO_FEEDBACK = '5'
    BATTERY_LEVEL = '68'
    BRIGHTNESS = '8'
    CARBON_DIOXIDE_DETECTED = '92'
    CARBON_DIOXIDE_LEVEL = '93'
    CARBON_DIOXIDE_PEAK_LEVEL = '94'
    CARBON_MONOXIDE_DETECTED = '69'
    CARBON_MONOXIDE_LEVEL = '90'
    CARBON_MONOXIDE_PEAK_LEVEL = '91'
    CHARGING_STATE = '8F'
    COLOR_TEMPERATURE = 'CE'
    CONTACT_STATE = '6A'
    DENSITY_NO2 = 'C4'
    DENSITY_OZONE = 'C3'
    DENSITY_PM10 = 'C7'
    DENSITY_PM25 = 'C6'
    DENSITY_SO2 = 'C5'
    DENSITY_VOC = 'C8'
    DOOR_STATE_CURRENT = 'E'
    DOOR_STATE_TARGET = '32'
    FAN_STATE_CURRENT = 'AF'
    FAN_STATE_TARGET = 'BF'
    FILTER_CHANGE_INDICATION = 'AC'
    FILTER_LIFE_LEVEL = 'AB'
    FILTER_RESET_INDICATION = 'AD'
    FIRMWARE_REVISION = '52'
    HARDWARE_REVISION = '53'
    HEATING_COOLING_CURRENT = 'F'
    HEATING_COOLING_TARGET = '33'
    HORIZONTAL_TILT_CURRENT = '6C'
    HORIZONTAL_TILT_TARGET = '7B'
    HUE = '13'
    IDENTIFY = '14'
    IMAGE_MIRROR = '11F'
    IMAGE_ROTATION = '11E'
    INPUT_EVENT = '73'
    LEAK_DETECTED = '70'
    LIGHT_LEVEL_CURRENT = '6B'
    LOCK_MANAGEMENT_AUTO_SECURE_TIMEOUT = '1A'
    LOCK_MANAGEMENT_CONTROL_POINT = '19'
    LOCK_MECHANISM_CURRENT_STATE = '1D'
    LOCK_MECHANISM_LAST_KNOWN_ACTION = '1C'
    LOCK_MECHANISM_TARGET_STATE = '1E'
    LOCK_PHYSICAL_CONTROLS = 'A7'
    LOGS = '1F'
    MANUFACTURER = '20'
    MODEL = '21'
    MOTION_DETECTED = '22'
    MUTE = '11A'
    NAME = '23'
    NIGHT_VISION = '11B'
    OBSTRUCTION_DETECTED = '24'
    OCCUPANCY_DETECTED = '71'
    ON = '25'
    OUTLET_IN_USE = '26'
    POSITION_CURRENT = '6D'
    POSITION_HOLD = '6F'
    POSITION_STATE = '72'
    POSITION_TARGET = '7C'
    RELATIVE_HUMIDITY_CURRENT = '10'
    RELATIVE_HUMIDITY_TARGET = '34'
    ROTATION_DIRECTION = '28'
    ROTATION_SPEED = '29'
    SATURATION = '2F'
    SECURITY_SYSTEM_ALARM_TYPE = '8E'
    SECURITY_SYSTEM_STATE_CURRENT = '66'
    SECURITY_SYSTEM_STATE_TARGET = '67'
    SELECTED_RTP_STREAM_CONFIGURATION = '117'
    SERIAL_NUMBER = '30'
    SERVICE_LABEL_INDEX = 'CB'
    SERVICE_LABEL_NAMESPACE = 'CD'
    SETUP_ENDPOINTS = '118'
    SLAT_STATE_CURRENT = 'AA'
    SMOKE_DETECTED = '76'
    STATUS_ACTIVE = '75'
    STATUS_FAULT = '77'
    STATUS_JAMMED = '78'
    STATUS_LO_BATT = '79'
    STATUS_TAMPERED = '7A'
    STREAMING_STATUS = '120'
    SUPPORTED_AUDIO_CONFIGURATION = '115'
    SUPPORTED_RTP_CONFIGURATION = '116'
    SUPPORTED_VIDEO_STREAM_CONFIGURATION = '114'
    SWING_MODE = 'B6'
    TEMPERATURE_COOLING_THRESHOLD = 'D'
    TEMPERATURE_CURRENT = '11'
    TEMPERATURE_HEATING_THRESHOLD = '12'
    TEMPERATURE_TARGET = '35'
    TEMPERATURE_UNITS = '36'
    TILT_CURRENT = 'C1'
    TILT_TARGET = 'C2'
    TYPE_SLAT = 'C0'
    VERSION = '37'
    VERTICAL_TILT_CURRENT = '6E'
    VERTICAL_TILT_TARGET = '7D'
    VOLUME = '119'
    ZOOM_DIGITAL = '11D'
    ZOOM_OPTICAL = '11C'

    def __init__(self):
        """Initialize the object."""
        self.baseUUID = '-0000-1000-8000-0026BB765291'
        self._characteristics = {
            '1': 'public.hap.characteristic.administrator-only-access',
            '5': 'public.hap.characteristic.audio-feedback',
            '8': 'public.hap.characteristic.brightness',
            'D': 'public.hap.characteristic.temperature.cooling-threshold',
            'E': 'public.hap.characteristic.door-state.current',
            'F': 'public.hap.characteristic.heating-cooling.current',
            '10': 'public.hap.characteristic.relative-humidity.current',
            '11': 'public.hap.characteristic.temperature.current',
            '12': 'public.hap.characteristic.temperature.heating-threshold',
            '13': 'public.hap.characteristic.hue',
            '14': 'public.hap.characteristic.identify',
            '1A': 'public.hap.characteristic.lock-management.auto-secure-'
                  'timeout',
            '1C': 'public.hap.characteristic.lock-mechanism.last-known-action',
            '1D': 'public.hap.characteristic.lock-mechanism.current-state',
            '1E': 'public.hap.characteristic.lock-mechanism.target-state',
            '1F': 'public.hap.characteristic.logs',
            '19': 'public.hap.characteristic.lock-management.control-point',
            '20': 'public.hap.characteristic.manufacturer',
            '21': 'public.hap.characteristic.model',
            '22': 'public.hap.characteristic.motion-detected',
            '23': 'public.hap.characteristic.name',
            '24': 'public.hap.characteristic.obstruction-detected',
            '25': 'public.hap.characteristic.on',
            '26': 'public.hap.characteristic.outlet-in-use',
            '28': 'public.hap.characteristic.rotation.direction',
            '29': 'public.hap.characteristic.rotation.speed',
            '2F': 'public.hap.characteristic.saturation',
            '30': 'public.hap.characteristic.serial-number',
            '32': 'public.hap.characteristic.door-state.target',
            '33': 'public.hap.characteristic.heating-cooling.target',
            '34': 'public.hap.characteristic.relative-humidity.target',
            '35': 'public.hap.characteristic.temperature.target',
            '36': 'public.hap.characteristic.temperature.units',
            '37': 'public.hap.characteristic.version',
            '52': 'public.hap.characteristic.firmware.revision',
            '53': 'public.hap.characteristic.hardware.revision',
            '64': 'public.hap.characteristic.air-particulate.density',
            '65': 'public.hap.characteristic.air-particulate.size',
            '66': 'public.hap.characteristic.security-system-state.current',
            '67': 'public.hap.characteristic.security-system-state.target',
            '68': 'public.hap.characteristic.battery-level',
            '69': 'public.hap.characteristic.carbon-monoxide.detected',
            '6A': 'public.hap.characteristic.contact-state',
            '6B': 'public.hap.characteristic.light-level.current',
            '6C': 'public.hap.characteristic.horizontal-tilt.current',
            '6D': 'public.hap.characteristic.position.current',
            '6E': 'public.hap.characteristic.vertical-tilt.current',
            '6F': 'public.hap.characteristic.position.hold',
            '70': 'public.hap.characteristic.leak-detected',
            '71': 'public.hap.characteristic.occupancy-detected',
            '72': 'public.hap.characteristic.position.state',
            '73': 'public.hap.characteristic.input-event',
            '75': 'public.hap.characteristic.status-active',
            '76': 'public.hap.characteristic.smoke-detected',
            '77': 'public.hap.characteristic.status-fault',
            '78': 'public.hap.characteristic.status-jammed',
            '79': 'public.hap.characteristic.status-lo-batt',
            '7A': 'public.hap.characteristic.status-tampered',
            '7B': 'public.hap.characteristic.horizontal-tilt.target',
            '7C': 'public.hap.characteristic.position.target',
            '7D': 'public.hap.characteristic.vertical-tilt.target',
            '8E': 'public.hap.characteristic.security-system.alarm-type',
            '8F': 'public.hap.characteristic.charging-state',
            '90': 'public.hap.characteristic.carbon-monoxide.level',
            '91': 'public.hap.characteristic.carbon-monoxide.peak-level',
            '92': 'public.hap.characteristic.carbon-dioxide.detected',
            '93': 'public.hap.characteristic.carbon-dioxide.level',
            '94': 'public.hap.characteristic.carbon-dioxide.peak-level',
            '95': 'public.hap.characteristic.air-quality',
            'A6': 'public.hap.characteristic.accessory-properties',
            'A7': 'public.hap.characteristic.lock-physical-controls',
            'A8': 'public.hap.characteristic.air-purifier.state.target',
            'A9': 'public.hap.characteristic.air-purifier.state.current',
            'AA': 'public.hap.characteristic.slat.state.current',
            'AB': 'public.hap.characteristic.filter.life-level',
            'AC': 'public.hap.characteristic.filter.change-indication',
            'AD': 'public.hap.characteristic.filter.reset-indication',
            'AF': 'public.hap.characteristic.fan.state.current',
            'B0': 'public.hap.characteristic.active',
            'B6': 'public.hap.characteristic.swing-mode',
            'BF': 'public.hap.characteristic.fan.state.target',
            'C0': 'public.hap.characteristic.type.slat',
            'C1': 'public.hap.characteristic.tilt.current',
            'C2': 'public.hap.characteristic.tilt.target',
            'C3': 'public.hap.characteristic.density.ozone',
            'C4': 'public.hap.characteristic.density.no2',
            'C5': 'public.hap.characteristic.density.so2',
            'C6': 'public.hap.characteristic.density.pm25',
            'C7': 'public.hap.characteristic.density.pm10',
            'C8': 'public.hap.characteristic.density.voc',
            'CB': 'public.hap.characteristic.service-label-index',
            'CD': 'public.hap.characteristic.service-label-namespace',
            'CE': 'public.hap.characteristic.color-temperature',
            '114': 'public.hap.characteristic.supported-video-stream-'
                   'configuration',
            '115': 'public.hap.characteristic.supported-audio-configuration',
            '116': 'public.hap.characteristic.supported-rtp-configuration',
            '117': 'public.hap.characteristic.selected-rtp-stream-'
                   'configuration',
            '118': 'public.hap.characteristic.setup-endpoints',
            '119': 'public.hap.characteristic.volume',
            '11A': 'public.hap.characteristic.mute',
            '11B': 'public.hap.characteristic.night-vision',
            '11C': 'public.hap.characteristic.zoom-optical',
            '11D': 'public.hap.characteristic.zoom-digital',
            '11E': 'public.hap.characteristic.image-rotation',
            '11F': 'public.hap.characteristic.image-mirror',
            '120': 'public.hap.characteristic.streaming-status',
        }

        self._characteristics_rev = \
            {self._characteristics[k]: k for k in self._characteristics.keys()}

    def __getitem__(self, item):
        if item.endswith(self.baseUUID):
            item = item.split('-', 1)[0]
            item = item.lstrip('0').upper()

        if item in self._characteristics:
            return self._characteristics[item]

        if item in self._characteristics_rev:
            return self._characteristics_rev[item]

        # raise KeyError('Item {item} not found'.format_map(item=item))
        return 'Unknown Characteristic {i}?'.format(i=item)

    def get_short(self, item: str):
        """
        Get short name from item number.

        :param item: item number
        :returns: short name
        """
        orig_item = item
        if item.endswith(self.baseUUID):
            item = item.split('-', 1)[0]
            item = item.lstrip('0').upper()

        if item in self._characteristics:
            return self._characteristics[item].split('.')[-1]

        return 'Unknown Characteristic {i}?'.format(i=orig_item)

    def get_uuid(self, item_name):
        """
        Get UUID from name.

        :param item_name: name of item
        :returns: uuid
        """
        if item_name in self._characteristics_rev:
            short = self._characteristics_rev[item_name]

        if item_name in self._characteristics:
            short = item_name

        medium = '0' * (8 - len(short)) + short
        long = medium + self.baseUUID
        return long


CharacteristicTypes = _CharacteristicTypes()
