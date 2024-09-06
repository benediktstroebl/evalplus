Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
assert remove_duplicates(numbers) == [1, 3, 4, 5]

numbers = [1, 2, 3, 4, 3, 5]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 5]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 3]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]
```

This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a test to verify the correctness of the output. Additionally, the tests in the above script create a list of numbers, and then call the remove_duplicates function to get the desired output.