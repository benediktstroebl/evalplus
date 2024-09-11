Here's a self-contained Python script that solves the problem:

```markdown
### Interspersing Numbers in a List

This script defines a function `intersperse` that inserts a number `delimeter` between every two consecutive elements of input list `numbers`.

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The modified list with the delimeter inserted between elements.
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # start the result with the first element
    for num in numbers[1:]:  # loop through the rest of the list
        result.extend([delimeter, num])  # insert the delimeter and the current number
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

You can save this script to a file (e.g., `intersperse.py`) and run it using Python (e.g., `python intersperse.py`). The script defines the `intersperse` function and includes example usage to demonstrate its behavior.