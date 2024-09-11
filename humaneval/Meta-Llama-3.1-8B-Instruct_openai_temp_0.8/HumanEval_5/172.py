```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    return result


if __name__ == "__main__":
    # Test cases
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input. It creates a new list where the delimeter is inserted between every two consecutive elements of the input list. The script then tests this function with the provided test cases.