```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    result = list(numbers)
    return result

# Test the function with various input sets
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [5, 6, 7, 8, 7]
numbers3 = [3, 2, 4, 5, 6]

print("Test 1:")
print(remove_duplicates(numbers1))  # Expected output: [1, 2, 3, 4]

print("Test 2:")
print(remove_duplicates(numbers2))  # Expected output: [5, 6, 7, 8]

print("Test 3:")
print(remove_duplicates(numbers3))  # Expected output: [3, 4, 5, 6]
```
This Python code defines a function called remove_duplicates that takes a list of integers as input and removes all duplicate elements from it using the set data manipulation technique. The function then returns the test the function with different input sets, and the output is printed to verify its correctness.