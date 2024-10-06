from typing import Any, Optional

class Animal:

    def __init__(
            self,
            animal_id: int,
            species: str,
            current_date: str,
            age: Optional[int] = None,
            ) -> None:
        self.health_status: Optional[str] = None,
        self.animal_id = animal_id
        self.species = species
        self.current_date = current_date
        self.age = age


    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass


    def get_animal_details(animal_id) -> dict[str, Any]:
        pass