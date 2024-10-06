from typing import Any

from migration_path import MigrationPath

class Migration:

    def __init__(
            self,
            migration_id: int,
            current_location: str,
            species: str,
            start_date: str,
            migration_path: MigrationPath
            
    ) -> None:
        self.status: str = "Scheduled",
        self.migration_id = migration_id
        self.current_location = current_location
        self.species = species
        self.migration_path = migration_path
        self.start_date = start_date


    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

