```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to insert between every two consecutive elements.
    
    Returns:
        List[int]: The list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimeter)
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension with the `itertools.chain.from_iterable` function to achieve the same result in a more concise way:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to insert between every two consecutive elements.
    
    Returns:
        List[int]: The list with the delimeter inserted.
    """
    return list(itertools.chain.from_iterable(zip(numbers, [delimeter]*(len(numbers)-1)))) if numbers else []

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```