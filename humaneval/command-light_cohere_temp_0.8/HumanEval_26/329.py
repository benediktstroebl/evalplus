```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.count(seen) == 1]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]


# Example usage:
numbers = [1, 2, 3, 2, 4, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
 ``` 
This Python code defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements from the list. It uses a distinct set data structure to keep track of elements that have been encountered before, then iterates through the input list and adds elements to the set if they are not already present and are not equal to the number of occurrences of the element. The function also includes a `test_remove_duplicates` function to verify the correctness of the `remove_duplicates` function.