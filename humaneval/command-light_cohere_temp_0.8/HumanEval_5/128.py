```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    >>> numbers = [1, 2, 3, 4, 3, 5]
    >>> intersperse(numbers, 2)
    [1, 2, 2, 3, 4, 3, 5]
    >>> intersperse([1, 2, 3], [3, 2])
    [1, 3, 3, 2, 4]
    >>> intersperse([1, 2, 3, 4], 'aaa')
    ['aaa', 1, 2, 3, 'aaa', 4]
    >>> intersperse([100, 200, 300], 0)
    []
    """
    return [num + delimiter if i < len(numbers) - 1 else delimiter for i, num, delimiter in zip(numbers, delimeter)]

# Test cases
numbers = [1, 2, 3, 4, 3, 5]
print(inperseperate(numbers, 2))  # Output: [1, 2, 2, 3, 4, 3, 5]

numbers = [1, 2, 3]
print(inperseperate(numbers, [3, 2]))  # Output: [1, 3, 3, 2, 4]

numbers = ['aaa', 1, 2, 3]
print(inperseperate(numbers, 'aaa'))  # Output: ['aaa', 1, 2, 3]

numbers = [100, 200, 300]
print(inperseperate(numbers, 0))  # Output: []
```
This Python script defines a function `inperseperate` that takes a list of numbers and a delimiter as input and returns a new list with the elements of the input list separated by the specified delimiter. The function uses the ole, 'delimiter' in every pair of elements and adds it to the list if the index is less than the length of the list.