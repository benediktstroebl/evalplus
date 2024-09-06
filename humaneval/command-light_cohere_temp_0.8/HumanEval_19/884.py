```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine, sorted from smallest to largest.
    Valid choices are choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    # Sort the list of numbers in ascending order
    numbers = [int(num) for num in numbers.
    return ' '.join(str(num) for num in sorted(numbers))

# Test cases
test_sort_numbers = []
test_cases = [
    "three one five",
    "zero seven eight nine",
    "six three four",
    "one two three four five six",
    "two six seven eight nine"
]

for test_case in test_cases:
    actual_sort = sort_numbers(test_case)
    assert actual_sort == " ".join(str(num) for num in sorted(int(test_case))))
```