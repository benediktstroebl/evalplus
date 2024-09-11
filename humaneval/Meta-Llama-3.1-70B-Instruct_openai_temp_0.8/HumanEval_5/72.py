```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with delimeter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i!= 0:
            result.append(delimeter)
        result.append(num)
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input. It iterates over the list of numbers, appending the delimeter before each number except the first one. The resulting list is then returned.

The script also includes two test cases to verify the correctness of the `intersperse` function. The expected outputs are printed to the console.