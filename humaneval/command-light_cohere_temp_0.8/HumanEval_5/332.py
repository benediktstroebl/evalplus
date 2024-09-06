Here's the self-contained Python script with a function `intersperse()` that inserts a number 'delimiter' between every two consecutive elements of the input list:
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

# Test cases
numbers = [1, 2,3]
print(intersperse(numbers, 4))  # Expected output: [1,4,2,4,3]

numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 4))  # Expected output: [1,4,2,4,5]

numbers = [1,2,3,4,5,6]
print(intersperse(numbers, 4))  # Expected output: [1,4,2,4,5,6]

numbers = [1,2,3,4,5,6,7]
print(interspere(numbers, 4))  # Expected output: [1,4,2,4,5,6]

numbers = [1,2,3,4,5,6,7,8]
print(intersperse(numbers, 4))  # Expected output: [1,4,2,4,5,6,8]
```

This script provides a function `intersperse()` that, given an input list of numbers and an integer `delimiter`, returns a new list with the numbers separated by the `delimiter`. The test cases demonstrate the expected outputs for different scenarios.