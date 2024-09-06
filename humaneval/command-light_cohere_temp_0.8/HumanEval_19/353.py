```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    full_split_string)
    numbers = list(map(int, numbers. numbers))
    numbers.sort()
    - return ''.join(numbers)

# test cases
test_cases = [
    "three one five",
    "six seven eight nine",
    "zero one three four five six",
    "one two three four five six seven eight nine"
]

for case in test_cases:
    result = sort_numbers(case)
    print(f"Case: {case} -> {result}")
```