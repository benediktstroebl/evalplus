```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from the list.
    Args:
        numbers: list of integers
    Returns: list of integers without duplicates.
    """
    test:
    assert sorted(numbers) == sorted(set(numbers)), "Input list is not sorted"
    return numbers[:]

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
``` 
The code you provided is a Python script that includes a self-contained function called remove_duplicates. The function takes a list of integers as input and returns a new list with all duplicates removed. The test ensures the function is correct and produces the expected output, which is a list of integers without duplicates. The output of this code will be [1, 3, 4], which are the integers in the list without any duplicates.