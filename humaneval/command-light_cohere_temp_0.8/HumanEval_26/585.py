Here is a Python script that includes a self-contained function to solve the problem of removing duplicate elements from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize Set to store unique integers
    unique_ints = set()
    result = []
    for num in numbers:
        if num not in unique_ints:
            unique_ints.add(num)
            result.append(num)
   
    return result
def test_remove_duplicates(input_list: List[int]) -> None:
    expected_result = [1, 3, 4]
    actual_result = remove_duplicates(input_list)
    assert actual_result == expected_result, "The expected result and actual result do not match!"
input_list = [1, 2, 3, 2, 4]
test_remove_duplicates(input_list)
```

This script includes a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The `test_remove_duplicates` function tests the `remove_duplicates` function with a sample input list and asserts that the expected and actual results are equal.