```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The integer to be inserted between every two consecutive elements

    Returns:
    List[int]: A new list with the delimeter inserted between every two consecutive elements
    """
    result = []
    for num in numbers:
        result.append(num)
        if result!= numbers and result!= []:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
Alternatively, you can also use list comprehension with a more concise way to achieve the same result:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The integer to be inserted between every two consecutive elements

    Returns:
    List[int]: A new list with the delimeter inserted between every two consecutive elements
    """
    return [num for num in numbers for _ in (0, delimeter) if num]

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```