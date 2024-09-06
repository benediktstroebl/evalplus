from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [char.lower() for char in numbers]
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers