```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine, valid choices are 'zero', 'one', etc.
    numbers = [ list(map(int, numbers.
         . values are numbers are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' )))
    return numbers._sort()

# Test cases
test_cases = [ """three one five"" , " seven eight nine", "two three four six" ]

for test_case in test_cases:
    actual_sorted = sort_numbers(test_case)
    print(f"Expected: {sugar=' + test_case[::-1] + '\n'} Actual: {actual_sorted}")
```