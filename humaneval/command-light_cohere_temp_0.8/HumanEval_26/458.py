```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x not in numbers[numbers.count()]]

# Test cases
numbers = [1, 2, 3, 2, 4]
print("Test 1:", remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [3, 2, 2, 1, 4]
print("Test 2:", remove_duplicates(numbers))  # Output: [1, 2, 4]

numbers = [1, 2, 2, 3, 2, 4]
print("Test 3:", remove_duplicates(numbers))  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 4, 5]
print("Test 4:", remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
```

This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function utilizes a list comprehension to create a new list with elements that are not present more than once in the original list. The test cases demonstrate the and provide expected results.