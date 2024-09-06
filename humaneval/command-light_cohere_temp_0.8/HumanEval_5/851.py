```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
   
    for idx, num in numbers:
        yield num
        yield delimeter
    return list(numbers)

# Test the function with example cases
numbers = [1, 2, 3]
print(f"The result is: {interperse(numbers, 4)}")  # [1, 4, 2, 4, 3]
numbers = [1, 2, 3, 4]
print(f"The result is: {interperse(numbers, 4)}")  # [1, 4, 2, 4, 3]
numbers = [1, 2, 3, 4, 5]
print(f"The result is: {interperse(numbers, 4)}")  # [1, 4, 2, 4, 5]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and it yields a new list with the specified delimiter between every two consecutive elements. The function uses an yield statement, which allows it to produce multiple values at once and then return them as a list. The `numbers` list can be easily modified with different sets of numbers and delimiters, and the output will reflect the changes accordingly.