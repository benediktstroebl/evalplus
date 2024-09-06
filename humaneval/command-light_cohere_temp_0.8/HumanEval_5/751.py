```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: List[int], a list of integers
        delimiter: int, the delimiter number to insert
    Returns:
        List[int], the list with numbers separated by the delimiter
    """
    res = []
    for i in range(len(numbers) - 1):
        res.append(numbers[i+delimiter])
        numbers.append(numbers[i+1])
    return res
# Test the function
numbers = [1, 2, 3, 4, 5]
print(f"Result: {list(interperse(numbers, 2))}")
```