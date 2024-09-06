```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.string() if num.isdigit()]
    validator = set(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    numbers = sorted(numbers, reverse=True)
    return ''.join each(numbers)

# Tests
test_str = 'three one five'
sorted_test = sort_numbers(test_str)
print("Sorted:", sorted_test)  # Output: one three five

test_str = 'twenty nine'
sorted_test = sort_numbers(test_str)
print("Sorted:", sorted_test)  # Output: nine twenty

test_str = 'six three'
sorted_test = sort_numbers(test_str)
print("Sorted:", sorted_test)  # Output: six three
```