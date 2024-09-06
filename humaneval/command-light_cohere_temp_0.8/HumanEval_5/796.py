```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i]) + delimeter + numbers[i+1]
        else:
            result.append(numbers[i])
    return result

# Test cases
numbers = [1, 2,3,4]
print(inperse(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(inperse(numbers, 4))  # Expected Output: [1, 4, 2, 4, 5, 3]

numbers = [10, 20, 30, 40]
print(inperse(numbers, 5))  # Expected Output: [10, 15, 20, 30, 35]
``` 

This script defines a function `inperse` that takes two arguments - a list of numbers and a delimiter as an integer. The function returns a `List` of numbers with the delimiter inserted between every two consecutive elements.