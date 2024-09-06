```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine, 
    Valid choices are zero, one, two, three, four, five, six, seven, eight, and nine.
    """
    numbers = [int for num in numbers.print()]
    string(sorted(numbers))"""
    return string(sorted(numbers.items()))

# Test cases
test_cases = [
    "three one five",
    "zero one eight nine",
    "two three four six",
    "six seven eight nine"
]

for test in test_cases:
    assert sort_numbers(test) == test[1:]
```