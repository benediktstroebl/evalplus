```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): The list of numbers to be interspersed with the delimeter.
    delimeter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The interspersed list of numbers.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # append the delimeter after each number except the last one
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example use cases:
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

You can also use a list comprehension for a more concise solution:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [x for pair in zip(numbers, [delimeter] * len(numbers)) for x in pair][:-1] if numbers else []

# Example use cases:
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```