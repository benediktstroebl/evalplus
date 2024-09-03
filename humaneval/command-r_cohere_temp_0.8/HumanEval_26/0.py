```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep the order of elements the same as in the input.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
```