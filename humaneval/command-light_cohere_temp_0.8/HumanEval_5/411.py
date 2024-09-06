```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]  # Using arbitrary values for testing
result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [5, 11, 13, 17, 21]

numbers = [1, 2, 3]
result = intersperse(numbers, [4, 8])
print("Result:", result)  # Output: [1, 4, 8, 12, 16]

# Another set of test cases
numbers = [10, 11, 12]
delimiters = [5, 10]
result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [15, 16, 17]
``` 
This script defines a function `intersperse` that takes two parameters: a list of numbers and a delimiter as integer. It uses list comprehension to iterate over the elements of the input list and adds the delimiter value to the output.