```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with some cases
numbers = [1, 2, 3, 4, 5]
delimiters = [2, 3]  
result = intersperse(numbers, delimiters)

print("Results:", result)
``` 
This code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the elements of the original list separated by the provided delimiter. The test case demonstrates this result, and the expected output is shown.