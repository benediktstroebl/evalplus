```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Converting to set to remove duplicates
    return list(numbers)

# Test case 1
test_case1 = [1, 2, 3, 2, 4]
assert remove_duplicates(test_case1) == [1, 3, 4]

# Test case 2
test_case2 = [1, 2, 3, 3, 4]
assert remove_duplicates(test_case2) == [1, 2, 3, 4]

# Test case 3
test_case3 = [1, 2, 3, 4, 5]
assert remove_duplicates(test_case3) == [1, 2, 3, 4]
```

This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function converts the` the list to a set to remove duplicates, and then converts it back to a list. This provides a tests to ensure the correctness of the function. The test cases aim to validate the `remove_duplicates` function's behavior by passing the test suite.