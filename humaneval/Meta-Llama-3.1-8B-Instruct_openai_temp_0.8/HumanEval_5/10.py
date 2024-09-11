```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The modified list with the delimeter inserted between consecutive elements.
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the last delimeter if the input list is not empty
    if numbers:
        result.pop()
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # Expected output: []
    print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It iterates over the input list, appending each number and the delimeter to the result list. After the loop, it removes the last delimeter if the input list is not empty. The script also includes test cases to verify the function's correctness.