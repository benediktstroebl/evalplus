```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimiter inserted.
    """
    return list(itertools.chain.from_iterable((num, delimiter) for num in numbers))[:-1]

# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script uses the `itertools.chain.from_iterable` function to create a new list that contains the elements from the input list `numbers` and the `delimiter` inserted between each element. The `[:-1]` at the end is used to remove the extra `delimiter` that would otherwise be appended to the end of the list.

Alternatively, you can use a simple list comprehension to achieve the same result:

```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result
```

This version of the function uses a loop to iterate over the input list `numbers`, appending each element to the `result` list and also appending the `delimiter` after each element except the last one.