```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases 

numbers = [1, 2, 3, 4]
delimiters = [2, 3]

result = intersperse(numbers, delimiters)
print("Result:", result) 

numbers = [4, 3, 2, 1]
delimiters = [1, 4]

result = intersperse(numbers, delimiters)
print("Result:", result) 

numbers = [0, 1, 2, 3, 4]
delimiters = [0, 5]

result = intersperse(numbers, delimiters)
print("Result:", result) 
```  The function `intersperse` takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by the given delimiter. The test cases demonstrate how the  this function works by adding the number of the list multiplied by the delimiter to each element in the input list.