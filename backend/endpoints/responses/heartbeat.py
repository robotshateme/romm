from typing_extensions import TypedDict


class WatcherDict(TypedDict):
    ENABLED: bool
    TITLE: str
    MESSAGE: str


class TaskDict(WatcherDict):
    CRON: str


class SchedulerDict(TypedDict):
    RESCAN: TaskDict
    SWITCH_TITLEDB: TaskDict


class MetadataSourcesDict(TypedDict):
    IGDB_API_ENABLED: bool
    MOBY_API_ENABLED: bool


class HeartbeatResponse(TypedDict):
    VERSION: str
    WATCHER: WatcherDict
    SCHEDULER: SchedulerDict
    ANY_SOURCE_ENABLED: bool
    METADATA_SOURCES: MetadataSourcesDict
