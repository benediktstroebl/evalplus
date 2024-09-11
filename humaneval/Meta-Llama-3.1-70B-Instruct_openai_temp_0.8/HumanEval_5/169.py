```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between elements.
    
    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a more concise version with a list comprehension:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between elements.
    
    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    return [x for pair in zip(numbers, [delimiter] * len(numbers)) for x in pair][:-1] if numbers else []

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In the concise version, we use `zip` to pair each number with the delimiter, then flatten the list of pairs using a nested list comprehension. We use `[:-1]` to remove the extra delimiter at the end. If the input list is empty, we return an empty list.