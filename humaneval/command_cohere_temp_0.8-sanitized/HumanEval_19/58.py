from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    return ' '.join(sorted(numbers))