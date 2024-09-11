```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The list of numbers to intersperse with the delimiter.
        delimiter (int): The number to insert between each pair of numbers.

    Returns:
        List[int]: The list with the delimiter inserted between each pair of numbers.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Don't append the delimiter after the last number
            result.append(delimiter)
    return result

# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

if __name__ == "__main__":
    print("All test cases pass.")
```

This script defines the `intersperse` function as specified, along with two test cases to verify its correctness. The function iterates over the input list, appending each number and the delimiter (if it's not the last number) to the result list. The test cases use the `assert` statement to verify that the function produces the expected output. If the output matches the expected output, the script prints "All test cases pass."