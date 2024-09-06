```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are string are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    """
    return numbers.split(" ").sort(numbers.split(" "zero one two three four five six seven eight nine"))

# Test the function with different inputs and validate the output
test_sort_numbers_valid = [
    "zero one two three four five six seven eight nine"
    , "four six seven nine 10"
    ,"01  100"
]

for nums, expected in test_sort_numbers_valid:
    actual = sort_numbers(nums)
    assert actual == expected, f"Incorrect output: {actual}, expected: {expected}"
```