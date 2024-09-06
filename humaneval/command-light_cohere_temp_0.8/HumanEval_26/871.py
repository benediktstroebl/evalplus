```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep only the BibTex format is required.
    """

    list comprehension is used to filter out duplicates.
    """
    new list that contains only the unique elements.
    """
    expected output:
    """
    [1, 3, 4]
    """
    return [n for n in numbers if n not in numbers[:]]
```