```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    >>> [1, 2, 3]
    >>> [1, 4, 2, 4, 3] 
    >>> [1, 1000, 3000] 
    >>> [4, 10, 40, 60] 
    """
    return [i+delimiter for i, delimiter in enumerate(zip(numbers, delimeter), 1))+[delimiter]]

# Test the function with a variety of inputs
print(inperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
print(inperse([1, 1000, 3000], 4))  # Output: [1, 1000, 3000]
print(inperse([4, 10, 40, 60], 10))  # Output: [4, 10, 40, 60]
```