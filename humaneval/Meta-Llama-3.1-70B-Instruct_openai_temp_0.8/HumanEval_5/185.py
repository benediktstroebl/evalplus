```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
    """
    return [x for pair in zip(numbers, itertools.repeat(delimiter)) for x in pair][:-1] if numbers else []

def main():
    # Test cases
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
    print(intersperse([10, 20, 30, 40, 50], 0))  # [10, 0, 20, 0, 30, 0, 40, 0, 50]

if __name__ == "__main__":
    main()
```

This script uses the `itertools.repeat` function to create an iterator that repeats the delimiter, then uses the `zip` function to pair each number with the delimiter. The list comprehension then flattens the pairs into a single list, and the `[:-1]` slice removes the extra delimiter at the end. If the input list is empty, the function returns an empty list.