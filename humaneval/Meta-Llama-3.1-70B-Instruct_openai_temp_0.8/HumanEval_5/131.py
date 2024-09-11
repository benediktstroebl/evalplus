```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): A delimiter number to be inserted.

    Returns:
    List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, we define a function `intersperse` that takes a list of numbers and a delimiter as input. We initialize an empty list `result` to store the output. We then iterate over the input list using `enumerate` to get both the index and the value of each element. We append each element to the `result` list, and if it's not the last element, we append the delimiter as well. Finally, we return the `result` list.

The test cases at the end of the script verify that the function works as expected.