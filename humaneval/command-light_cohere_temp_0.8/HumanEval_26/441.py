```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only the particular as in the input.
    """
    return [set of [i for i, j in zip(numbers, numbers) if i != j] + numbers[j:]
    """
    # Discard duplicates using set difference.
    return [set(numbers) - set(numbers)
```

This function takes a list of integers as input and returns a new list with all the distinct integers from the original list. It uses the set difference to first remove any duplicate values, and then add the remaining unique values back together.