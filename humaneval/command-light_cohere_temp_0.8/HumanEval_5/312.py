```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    :param numbers: List[int], delimiter: int
    :return: List[int]
    """
    return [num + delimiter for num, delimiter in zip(numbers, delimeter)]

# Test the function with a variety of inputs
numbers = [1, 2, 3, 4, 10, 2, 5, 1]
print(inperseprse(numbers, 2))  # Expected Output: [1, 2, 3, 4, 10, 12, 5, 13]
```