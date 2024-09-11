```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimeter (int): The number to intersperse between the elements of `numbers`.
        
    Returns:
        List[int]: The list with `delimeter` interspersed between each pair of elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

Alternatively, you could use a list comprehension and the `itertools.chain` function to achieve the same result:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimeter (int): The number to intersperse between the elements of `numbers`.
        
    Returns:
        List[int]: The list with `delimeter` interspersed between each pair of elements.
    """
    return list(itertools.chain(*[[num, delimeter] if i < len(numbers) - 1 else [num] for i, num in enumerate(numbers)]))

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```