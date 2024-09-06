from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(char.lower()) for char in numbers]
    numbers.sort()
    return ' '.join(map(str, numbers))