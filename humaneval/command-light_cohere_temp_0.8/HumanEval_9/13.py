```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment.
    >>> [1, 2, 3, 3, 3, 4, 4]
    """
    return [n for n, _ in enumerate(sorted(numbers)) if _ <= num]

# Test cases:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 6, 7, 8, 9]
numbers3 = [10, 20, 30, 40, 50]

# Test function call:
result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)
result3 = rolling_max(numbers3)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
```
This script defines a function called `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements found in that list. The `test_cases` module is used to define test cases with different lists of integers. The function is then called with these test cases and the results are printed to the console.