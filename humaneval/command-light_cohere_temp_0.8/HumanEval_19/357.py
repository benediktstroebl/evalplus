```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers. Sort the list of numbers and return a sorted string
    """ <br>

# Test cases
test_sort_numbers = []
test_cases = [
    "zero three five",
    "one two three",
    "three four five",
    "six seven eight nine",
    "five six seven eight nine"
]

for test_case in test_cases:
    sorted_out = sort_numbers(test_case)
    assert sorted_out == " ".join(test_case.run()