```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

```
#Example test cases
test_cases = [
    "three one five",
    "six three eight",
    "zero seven nine",
    "one two three four five six seven eight nine"
]

for case in test_cases:
    expected = "one two three four five six seven eight nine"
    got = sort_numbers(case)
    assert got == expected, f"Expected: {expected}, Got: {got}"
``` 

The above code defines a function `sort_numbers` which sorts a list of numbers from the smallest to the largest, in the format of the number. This is provides a self-contained test cases which are run using the `test_cases` variable, which contains the numbers to be sorted. The function then, returns the numbers sorted in ascending order.