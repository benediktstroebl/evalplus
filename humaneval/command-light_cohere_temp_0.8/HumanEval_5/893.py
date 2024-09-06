```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result.append(num + delimeter)  # Odd index, add delimiter
        else:
            result.append(num)  # Even index, just append
    return result

# Test case 1: Using list with even elements
test_case1 = [1, 2, 3, 4, 5]
result1 = intersperse(test_case1, 2)
print(result1)  # Expected output: [1, 2, 3, 4, 5]

# Test case 2: Using empty list
test_case2 = []
result2 = intersperse(test_case2, 2)
print(result2)  # Expected output: []

# Test case 3: Using list with odd elements
test_case3 = [1, 3, 2, 4, 5]
result3 = intersperse(test_case3, 2)
print(result3)  # Expected output: [1, 3, 2, 4, 5] with 2 separating each odd element
``` 
This Python code defines a function `intersperse` that takes a list of integers and a delimiter as input. It iterates through list elements to separate consecutive elements with the specified delimiter, adding the delimiter for odd indices and directly appending for even indices. The code then provides three test cases to demonstrate the functionality, checking that the output aligns with the expected results.