```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with delimeter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        # If it's not the last number, add the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

You can run this script directly in your Python environment. It defines the `intersperse` function as specified in the problem statement and includes test cases to demonstrate its correctness.