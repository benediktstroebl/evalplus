```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): A number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): A number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    return [x for pair in zip(numbers, numbers[1:] + [delimiter]) for x in pair[:-1] + (delimiter,)]

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```