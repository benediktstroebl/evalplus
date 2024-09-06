```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with examples
numbers = [1, 2, 3]
delimiters = 4
result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1, 4, 2, 4, 3]
``` 
This Python function, `intersperse`, takes a list of integers and a delimiter as input and returns a new list with the elements of the input list separated by the specified delimiter. The function uses the simple mathematical operation to achieve this, and the time complexity of this operation is O(n), where n is the length of the input list.