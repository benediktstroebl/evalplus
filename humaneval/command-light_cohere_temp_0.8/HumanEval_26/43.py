```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers and return the unique elements.
    Input: numbers List
    Output: List[int]
    """
    # Remove duplicates
    numbers = list(set(numbers))
    # Return the unique elements
    return numbers
```