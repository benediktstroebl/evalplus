import unittest
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))