```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    expected = [1, 3, 4]
    actual = remove_duplicates(numbers)
    assert expected == actual


# Example usage
numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))
``` 
This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function uses a set to keep track of seen numbers and a list comprehension to filter out non-zero values that are not in the set. The function then returns the final list.