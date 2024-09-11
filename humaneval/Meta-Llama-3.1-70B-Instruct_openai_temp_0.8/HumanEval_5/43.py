```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Append the current number to the result
        result.append(num)
        
        # If it's not the last element in the list, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the modified list
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can also use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    
    # Use list comprehension to create the result
    return [x for pair in zip(numbers, [delimiter] * (len(numbers) - 1)) for x in pair] + ([numbers[-1]] if numbers else [])


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```