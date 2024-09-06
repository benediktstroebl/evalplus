```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the It elements left as in the input.
    return a list of unique elements
    """
    numbers = set(numbers)
    unique_elements = [element for element in numbers if element not in numbers.
    return [set([element for element in unique_elements])
```