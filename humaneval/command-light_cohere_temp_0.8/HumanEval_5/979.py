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
numbers = [1, 2,3,4]
print(inperse(numbers, 2))  # Expected Output: [1,2,3,4,2,4,3]

numbers = [4,9,2,6,5]
print(inperse(numbers, 6))  # Expected Output: [4,6,9,2,5,6,9]

numbers = [1,2,3,4,5,6]
print(inperse(numbers, 3))  # Expected Output: [1,2,3,4,5,6]

numbers = [1,2,3,4,5,6,7]
print(inperse(numbers, 2))  # Expected Output: [1,2,3,4,5,6,7]
```

The provided Python code defines a function `inperse()` that separates a list of numbers using a specified delimiter. It iterates through numbers and, if the index is even, appends the current number to the result list followed by the delimiter. If the index is odd, it appends the current number to the result list. The code also includes several test cases to demonstrate the functionality of the `inperse()` function.