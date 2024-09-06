```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n+
        if i < len(numbers) - 1 else delimeter)
    return result

# Test cases
numbers = [1, 2, 3]
delimiters = [4, 4, 8]  
result = intersperse(numbers, delimiters)
print(result)        # Expected output: [1, 4, 8, 2, 8, 3]
numbers = [1, 2, 3]
delimiters = [4]
result = intersperse(numbers, delimiters)
print(result)        # Expected output: [1, 4, 2, 4, 3]
``` 
This script defines a function `intersperse` that inserts a `delimiter` between every two consecutive elements in the `numbers` list. The function is then tested with several test cases, and the expected output is printed.