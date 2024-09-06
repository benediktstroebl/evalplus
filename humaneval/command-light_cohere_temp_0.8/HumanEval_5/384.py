Here is a Python script that solves the markdown code block provided:
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+delimiter for num, delimiter in zip(numbers, [delimeter]*2)]
# Test the function with different inputs
numbers = [4, 2, 3]
print(inperse ,numbers) 
# Test with different delimiters
numbers = [1, 2, 3]
print(inperse ,numbers, "/")
``` 
This script defines a function `inperse` that takes a list of numbers and a delimiter as input, and returns a new list with the numbers separated by the provided delimiter.  The function uses the process to iterate through the list of numbers and the corresponding delimiter, and returns a new list with each pair of elements separated by the delimiter.