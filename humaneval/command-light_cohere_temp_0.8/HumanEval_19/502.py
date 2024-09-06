```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    if set(numbers) == {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}:
        return numbers[::-1].join(' ')
    else:
        raise ValueError("Invalid input")
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Test case 1: Valid input
test_case1 = "three one five"
sorted_result = sort_numbers(test_case1)
assert sorted_result == "one three five"
# Test case 2: Invalid input
test_case2 = "abc123"
try:
    sorted_result = sort_numbers(test_case2)
except ValueError as e:
    print(e)
```