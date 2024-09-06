```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string is like 'zero one two three four five six seven eight nine'
    Valid numbers are a subset of these strings
    """
    return "".join("zero" + numbers + " nine")

# Test cases
test_cases = [
    "three one five",
    "six seven eight nine",
    "zero",
    "one",
    "two three four five six seven eight nine",
    " fool ",
    "nine"
]

for i, test in enumerate(test_cases):
    result = sort_numbers(test)
    print(f"Test {i+1}: {test} should be {result}")
```