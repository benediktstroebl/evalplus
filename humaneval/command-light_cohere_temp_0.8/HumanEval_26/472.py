```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]  # else num]

# Sample test cases
test_remove_duplicates_cases = [
    [],  # [] and any other empty list will return [].
    [1, 2, 3, 2, 4],
    [1, 3, 2, 4, 5],
    [10, 20, 30],  # Long list with duplicates
]

for test_case in test_remove_duplicates_cases:
    expected = [1, 3, 4]  # Removed duplicates
    actual = remove_duplicates(test_case)
    assert actual == expected, "TestCase {} failed".
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The function uses the use a set data structure to keep track of duplicate elements and then uses list comprehension to filter out all elements that are not present in the set. The test cases cover a empty lists, lists with duplicates, and longer lists. The test cases are passed to the `remove_duplicates` function and the results are compared with the expected output to verify that the function is working correctly.