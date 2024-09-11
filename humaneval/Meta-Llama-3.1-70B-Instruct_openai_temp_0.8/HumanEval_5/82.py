```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): Input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result


def main():
    print(intersperse([], 4))  # Expected output: []
    print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]


if __name__ == "__main__":
    main()
```

In this script, we define a function `intersperse` that takes a list of numbers and a delimiter as input. It iterates over the list, appending each number to the result and the delimiter if it's not the last number in the list. The `main` function provides example use cases for this function. The script uses a `if __name__ == "__main__":` block to ensure that the `main` function is only executed when the script is run directly, not when it's imported as a module.