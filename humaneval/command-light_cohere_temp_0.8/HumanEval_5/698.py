```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test the function with a sample input and output
numbers = [1, 2, 3,4]
print(inperse(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]

numbers = [10, 9, 8, 7]
print(inperse(numbers, 4))  # Expected Output: [10, 9, 8, 7]

numbers = [1, 2, 3]
print(inperse(numbers, 3))  # Expected Output: [1, 2, 3]

numbers = [10, 9, 8, 7]
print(inperse(numbers, 3))  # Expected Output: [10, 9, 8]
``` 
This Python code defines a function `inperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers interspaced by the delimiter. The code provides several test cases to validate the correctness of the `inperse` function.