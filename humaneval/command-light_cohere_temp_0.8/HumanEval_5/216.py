```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with different inputs and verify the output
numbers_test = [3, 2, 1, 4, 5]
delimiters_test = [2, 3]  

result_test = intersperse(numbers_test, delimiters_test)
print(result_test)  # Expected Output: [2, 4, 4, 5, 8, 10]
```