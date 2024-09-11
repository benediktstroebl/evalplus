```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The resulting list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Only append the delimeter if it's not the last element
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines the `intersperse` function, which takes a list of integers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, appending each number and the delimeter (if it's not the last element) to the result list.

Alternatively, you could use a list comprehension to implement the `intersperse` function in a more concise way:

```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimeter) if x is not None]
```
This version of the function uses the `zip` function to pair each element in the input list with the next element, and then uses a nested list comprehension to flatten the pairs and insert the delimeter. The `[None]` is added to the end of the list to ensure that the delimeter is not appended after the last element.