```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): A list of integers
        delimeter (int): The number to insert between consecutive elements

    Returns:
        List[int]: A list of integers with the delimeter inserted between consecutive elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input. It iterates over the input list, appending each number and the delimeter to the result list. If it's not the last element in the list, it appends the delimeter. The function then returns the result list. The example usage at the end demonstrates how to use this function with the provided test cases.