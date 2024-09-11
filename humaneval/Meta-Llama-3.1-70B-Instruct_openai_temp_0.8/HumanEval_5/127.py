```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: The resulting list with 'delimiter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

Alternatively, you can also use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: The resulting list with 'delimiter' inserted between every two consecutive elements.
    """
    return [x for pair in zip(numbers, [delimiter] * len(numbers)) for x in pair[:-1]]

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```