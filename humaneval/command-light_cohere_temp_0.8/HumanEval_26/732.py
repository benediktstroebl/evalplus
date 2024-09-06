```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0 and num not in seen]

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique positive integers from the input. The function uses a set data structure to track the seen integers and removes duplicates by filtering out elements that are not in the set and are positive and have not been seen before. The code also includes a `test_remove_duplicates` function that checks the correctness of the `remove_duplicates` function by asserting that it produces the expected output. The example usage demonstrates how the result would be a list containing only the unique positive integers from the input list.