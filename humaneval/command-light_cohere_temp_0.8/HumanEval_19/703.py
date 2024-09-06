Here is a Python script that contains a self-contained function that sorts and returns a list of numbers in descending order:
```python
from typing import List

def sort_numbers(numbers: List[int]) -> List[int]:
    return [num for num in reversed(sorted(numbers))]

# Test the function with a sample input
numbers = [3, 1, 5]
print(sort_numbers(numbers))  # Output: [5, 3, 1]
```
This function, named `sort_numbers`, takes a list of integers as input and returns a new list with the numbers sorted in descending order.