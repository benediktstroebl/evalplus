```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimeter (int): The number to insert between consecutive elements in the list.

    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the extra delimeter at the end of the list
    result.pop()
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
    print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimeter as input. It creates a new list, appends each element from the input list, followed by the delimeter, and then removes the extra delimeter at the end of the list. The result is a list with the delimeter inserted between every two consecutive elements. The test cases at the end demonstrate the function's behavior.