__author__ = 'dwayn'


class SshManagerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotConnected(SshManagerError):
    pass

class FailedAuthentication(SshManagerError):
    pass


class StorageManagerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InstanceNotFound(StorageManagerError):
    pass

class VolumeNotAvailable(StorageManagerError):
    pass

class VolumeGroupNotFound(StorageManagerError):
    pass

class RaidError(StorageManagerError):
    pass

class VolumeMountError(StorageManagerError):
    pass

class SnapshotError(StorageManagerError):
    pass

class SnapshotCreateError(SnapshotError):
    pass


