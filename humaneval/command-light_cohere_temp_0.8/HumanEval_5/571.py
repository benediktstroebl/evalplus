```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)] + numbers[:-len(numbers)//2]

# Test cases 

numbers = [1, 2, 3, 4, 5]
print(inperseperate(numbers, 4))  # Expected: [1, 4, 2, 4, 3, 5]

numbers = [1, 2, 3, 4, 5, 6]
print(inperseperate(numbers, 4))  # Expected: [1, 4, 2, 4, 3, 6]

numbers = [10, 11, 12, 13]
print(inperseperate(numbers, 4))  
# Expected: [10, 9, 11, 13]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(inperseperate(numbers, 8))  
# Expected: [1, 8, 2, 8, 3, 8, 4, 8, 5, 8, 6]
``` 
The provided Python script defines a function called **'inperseperate()'** that takes a list of numbers and a delimiter as input and returns a new list with the elements of the original list, with the delimiter inserted between every other consecutive element. The test cases demonstrate the result of the function, passing different lists and delimiters, and the expected output is printed to the console.