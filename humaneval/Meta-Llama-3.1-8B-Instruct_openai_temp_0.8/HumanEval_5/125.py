```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    
    return result


# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]
```

This Python function works by checking if the input list is empty. If it is, the function returns an empty list. If the list is not empty, the function starts by inserting the first element of the list into the result. Then, it iterates over the rest of the list, inserting the delimeter and each number into the result after the last number has been processed. This approach ensures that the delimeter is inserted between every two consecutive elements in the input list.