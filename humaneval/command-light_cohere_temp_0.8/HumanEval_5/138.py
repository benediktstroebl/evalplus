```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num] + [delimeter] * (len(numbers) - 2) + [num]
    return result

# Test the function with various inputs
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 0, 1, 1, 2] 

# Run the function with different combinations of numbers and delimiters
for delimiter in delimiters:
    for num in numbers:
        expected = [num] + [num] + [delimiter] + [num]
        actual =   intersperse(numbers, delimiter)
        assert actual == expected, f"Failed for {num}, {delimiter}"

# We've passed all tests successfully!
print("All tests passed")
```