```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the how elements left as in the input.
    return [a new list with unique values.
    """
    essential input is just a list of integers"""
    return [i for i in numbers if numbers.count(i) == 1]
```

This code provides a self-contained function to remove duplicates from a list of integers. The function utilizes a built-in function `count` to get the number of occurrences of each element and then returns a new list with only the unique elements.