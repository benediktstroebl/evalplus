```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as in the input.
    return [set of numbers[:-1]]
    """
    seen = set()
    result = [x for x in numbers if x not in seen and x not in result]
    seen.add(numbers)
    return result
```
The function removes duplicate integers from the input list and returns a new list with unique values.