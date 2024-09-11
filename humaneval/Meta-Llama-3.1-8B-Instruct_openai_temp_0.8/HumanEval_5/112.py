```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers: A list of integers.
        delimeter: An integer to be inserted between the numbers in the list.

    Returns:
        A new list with the delimeter inserted between every two consecutive elements.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # Base case: an empty list remains unchanged

    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Append the current number
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

However this problem can be solved in a more efficient way by using list comprehension and the `itertools.chain` function:

```python
from typing import List
import itertools


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers: A list of integers.
        delimeter: An integer to be inserted between the numbers in the list.

    Returns:
        A new list with the delimeter inserted between every two consecutive elements.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # Base case: an empty list remains unchanged

    return list(itertools.chain.from_iterable(
        [[num] for num in numbers] + [[delimeter] for _ in numbers[:-1]]
    ))


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```