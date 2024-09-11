```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the extra delimeter at the end
    result.pop()
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. The script also includes test cases to verify the function's correctness.