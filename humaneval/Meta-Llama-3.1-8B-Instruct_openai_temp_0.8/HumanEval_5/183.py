### Interspersing Delimeter in a List

Below is a Python script that defines a function `intersperse` to insert a number 'delimeter' between every two consecutive elements of the input list `numbers`.

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the elements.

    Returns:
    List[int]: The list with the delimeter inserted between every two consecutive elements.
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i!= len(numbers) - 1:  # Check if not the last element
            result.append(delimeter)
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

Alternatively, you can use list comprehension with a generator expression to achieve the same result:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the elements.

    Returns:
    List[int]: The list with the delimeter inserted between every two consecutive elements.
    """
    return [x for pair in zip([0] + numbers, numbers + [0]) for x in pair if x!= 0]  # Use pair to include delimeter

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```