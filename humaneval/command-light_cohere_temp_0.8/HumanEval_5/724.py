```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    - If delimiter is zero, numbers will not be split at all
    - Negative values are treated as zero for splitting
    """
    if delimeter <= 0:
        return numbers
    return [num + i * delimeter for i, num in enumerate(numbers)] + [delimiter]

# Test the function with sample inputs and desired output
numbers = [1, 2, 3, 4, 5]
desired_output = [1, 4, 2, 4, 3, 6]
print(invisalign(numbers, 3))  # expected output: [1, 4, 2, 4, 3, 6]
```