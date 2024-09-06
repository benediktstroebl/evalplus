```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: list of integers,
        delimiter: positive integer

    Returns:
        list of integers
    """
    numbers.length = len(numbers)
    result = [numbers[i]] + [numbers[i+1]] + [numbers[i]]  # start, end, repeat
    while i < length - 1:
        i += 1
        result.append(numbers[i]) + [numbers[i+1]] + [delimiter]  # append start, end, current, repeat
    return result
``` 
This code defines a Python function called **'intersperse()'** that takes a list of integers **'numbers'`** and an integer **'delimiter'** as input. It creates a
list of integers and inserts a number **'delimiter'** between every two consecutive elements. The code then repeats this process until it reaches the end of the list, appending the start, end, current number, and repeat (created by [numbers[i], numbers[i+1], delimiter] to the result list. 

This is a self-contained solution to the provided problem statement.