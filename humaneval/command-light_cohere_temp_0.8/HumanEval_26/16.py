```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    numbers = [1, 2, 3, 2, 4, 1]
    return [x for x in numbers if x < numbers.count(numbers)]
```
The function removes duplicate elements from the input list and returns a new list with unique elements.