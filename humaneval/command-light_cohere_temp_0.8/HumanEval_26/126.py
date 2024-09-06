```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [set of numbers without duplicates"""
    numbers = set(numbers)
    return list(numbers)

# Test cases
test_remove_duplicates = []
test_remove_duplicates.append([1, 2, 3, 2])
test_remove_duplicates.append([4, 4, 4])
test_remove_duplicates.append([5, 1])
test_remove_duplicates.append([1, 3, 4, 1])

# Call the function and compare the output with the expected results
for test in test_remove_duplicates:
    actual = remove_duplicates(test)
    assert actual == test

print("All tests passed!")
```