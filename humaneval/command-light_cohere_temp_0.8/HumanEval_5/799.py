```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.

    : O(n), Input: list
    on O(n) Output: list
    """
    # Insert the delimiter in a new list
    delimiter_list = [num + delimeter for num in numbers]
    return delimiter_list

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiter = 4

result = intersperse(numbers, delimiter)
print("Result:", result)

expect = [1, 4, 2, 4, 3, 5]
print("Expect:", expect)
```  This code provides a function `intersperse` that inserts a specified delimiter between every two consecutive elements of a given list.  The tests to demonstrate this function with a simple list of numbers and compares the expected results against the actual results.