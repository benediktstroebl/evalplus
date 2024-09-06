from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)