```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with some sample inputs
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)

# Print the result
print(result)
```  This code defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list where every element is separated by the specified delimiter. The function uses a simple iteration and the sum of the delimiter to achieve this effect.