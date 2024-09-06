```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers. We'll use the foregoing string of numbers separated by spaces from 'zero' to 'nine'. The function uses the typing module to create a function that takes a string of numbers and returns a sorted version of the numbers. The test case is passed in and the function returns the sorted version of the string.

# Test cases
numbers = "three onefive"
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Output: "one threefive"
numbers = "3089"
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Output: "zero eight nine"
```