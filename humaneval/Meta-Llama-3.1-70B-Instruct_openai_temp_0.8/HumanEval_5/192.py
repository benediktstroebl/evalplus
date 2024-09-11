```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between elements.
    
    Returns:
        A new list with the delimiter inserted between every two elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result
        result.append(num)
        
        # If it's not the last element, add the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the resulting list
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
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between elements.
    
    Returns:
        A new list with the delimiter inserted between every two elements.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimiter) if x is not None]

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```