```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimiter)
        else:
            result.append(numbers[i])
    return result

# Test cases
numbers = [1, 2,3]
print(inperse(numbers, 2))  # Expected output: [1,2,2,3]

numbers = [1, 2, 3,4,3]
print(inperse(numbers, 2))  # Expected output: [1,2,3,4,3]

numbers = [1, 2, 3, 4]
print(inperse(numbers, 4))  # Expected output: [1,2,4,3]

numbers = [1, 2, 3, 4, 5]
print(inperse(numbers, 4)) # Expected output: [1,2,4,5]
``` 
This Python script defines a function `inperse` which takes a list of numbers and a delimiter as input and returns a list where every odd index of the number receives the delimiter and the rest are appended. This script provides several test cases to validate the `inperse` function, and the expected output matches the problem statement.