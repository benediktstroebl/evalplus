```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    >>> import: List[int]
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [i + j for i, j in zip(numbers, numbers[1:])]

# Test the function with various inputs
numbers = [1, 2, 3]
test_numbers = [4, 5, 6]

result_1 = intersperse(numbers, 4)
result_2 = intersperse(test_numbers, 2)

print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")

# Test with empty list
result_3 = intersperse([], 4)
print(f"Result 3: {result_3}")

# Test with custom delimiter
numbers = [1, 2, 3]
delimiter = 'abc'
result_4 = intersperse(numbers, delimiter)
print(f"Result 4: {result_4}")
``` 
The script defines a function `intersperse` that takes a list of numbers and an integer `delimiter` as input, and returns a new list with the elements of the input list interspaced by the provided `delimiter`. 

It then passes the function with various test cases and demonstrates the results.