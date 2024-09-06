```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])] + [numbers[-1]]
# Test cases
numbers = [1,2,3]
print(intersperse(numbers,4))  # Expected output: [1,4,2,4,3]

numbers = [10, 9, 8, 7]
print(intersperse(numbers,4))  # Expected output: [10,9,8,7] , [10, 9, 8, 7] 

numbers = [7,6,5]
print(intersperse(numbers,4))  # Expected output: [7,6,5], [7, 6, 5] 

numbers = [10,10,10]
print(intersperse(numbers,2))  # Expected output: [10, 10, 10] 
``` 
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the numbers interspaced by the provided delimiter. The test cases demonstrate the