```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i > 0: result.append(delimiter)
        result.append(num)
   
    return result

# Test the function with example input
numbers = [1, 2, 3]
delimiter = 4
solution = intersperse(numbers, delimiter)
print(solution)  # Output: [1, 4, 2, 4, 3]
``` 
This script defines a function `inseperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by the specified delimiter. The script then provides an test case with the function using the same input values, and the output is displayed.