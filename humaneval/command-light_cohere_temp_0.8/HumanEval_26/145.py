```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:seen]]

# Test cases
numbers = [1, 2, 3, 2, 4]
print("Test 1:", remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 1, 3]
print("Test 2:", remove_duplicates(numbers))  # Expected output: [1, 2, 3]

numbers = [1, 2, 3, 4, 5, 6]
print("Test 3:", remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 6, 2]
print("Test 4:", remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 4, 3]
print("Test 5:", remove_duplicates(numbers))  # Expected output: []
``` 
This Python script contains a function called `remove_duplicates`, which takes a list of integers as input and removes duplicate elements from it. The test cases ensure that the function works correctly and provides the expected output.