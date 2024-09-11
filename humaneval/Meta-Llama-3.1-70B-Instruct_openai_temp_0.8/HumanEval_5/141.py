```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted.
    
    Returns:
    List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # Expected: []
print(intersperse([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted.
    
    Returns:
    List[int]: The modified list with the delimiter inserted.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimiter) if pair[0] is not None]

# Test cases
print(intersperse([], 4))  # Expected: []
print(intersperse([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
```

Both of these scripts will insert the specified delimiter between every two consecutive elements in the input list. If the input list is empty, the function will return an empty list.