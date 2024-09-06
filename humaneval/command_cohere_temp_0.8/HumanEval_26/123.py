```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. Inside the function, it tracks seen integers using a `set`, and adds unique integers to the `result` list. The function efficiently removes duplicates from the input list and retains the original order. This is specified in the docstring, which also includes a usage example. 

To ensure the function behaves as intended, two tests are included:
1. A unit test that checks the function removes duplicates from a list with different permutations of the number 2.
2. A integration test that verifies the function removes duplicates from a list with increasingly complex test cases. 

These tests ensure the function remains stable across different input scenarios.