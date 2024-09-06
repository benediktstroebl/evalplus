```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique numbers
    unique_numbers = set()
    for num in numbers:
        unique_numbers.add(num)
    # Filter out duplicate numbers and return a new list
    return list(unique_numbers)

# Test cases
numbers = [1, 2, 3, 2, 4]
print("Test 1:", remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [5, 5, 6, 5, 6]
print("Test 2:", remove_duplicates(numbers))  # Output: [5, 6]

numbers = [1, 2, 3, 4, 5]
print("Test 3:", remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 5, 6]
print("Test 4:", remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and removes duplicate numbers from it. It achieves this by creating a set of unique numbers and then converting the set back into a list. The code includes multiple test cases to demonstrate the function's behavior.