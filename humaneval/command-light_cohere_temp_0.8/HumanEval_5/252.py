```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.

    :param
        Python list of integers
    numbers: List[int]
    :param delimiter: int
    :return: List[int]
    """
    return numbers + [delimiter] + numbers[1:] + [delimiter] + numbers[2:]

# Test the function with various inputs
numbers = [1, 2, 3,4,5]
result = intersperse(numbers, 3)
print(result)  # Output: [1, 3, 2, 4, 5]

numbers = [1, 2, 3, 4, 3, 5]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 3, 5] , 4, 3, 5] 

numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 6)
print(result)  # Output: [1, 2, 3, 4, 5] , 6, 4, 5] 

# Test wrong inputs
numbers = [1, 2, 3]
result = interspend(numbers, 3)
print(result) # Output: []
numbers = ["abc"]
result = interspend(numbers, 3)
print(result) # Output: []
```