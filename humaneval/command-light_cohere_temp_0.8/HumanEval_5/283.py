```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*delimeter for i,num in enumerate(numbers)]

# Test cases
numbers = [1,2,3]
print("Input numbers:",numbers)
print("Expected Output:",intersperse(numbers,2))

numbers = [1,2,3,4]
print("Input numbers:",numbers)
print("Expected Output:",intersperse(numbers,3))

numbers = [1,2,3,4,5]
print("Input numbers:",numbers)
print("Expected Output:",intersperse(numbers,2))
```

This code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a list of integers with the specified delimiter between every two consecutive elements. The code then passes the use three test cases to demonstrate the functionality of the `intersperse` function.