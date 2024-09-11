```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between consecutive elements

    Returns:
        List[int]: The list with the delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the last occurrence of the delimeter
    result.pop()
    return result

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

However, if you want a more concise version of the function, you can use list comprehension and list slices:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between consecutive elements

    Returns:
        List[int]: The list with the delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    return [num for num in numbers + [delimeter] for _ in range(2)][:-1]

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```