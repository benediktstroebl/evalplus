```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

```
numbers = ["three", "one", "five"]
test_numbers = ["zero", "one", "two", "three", "four", "five"]

# Call the sort_numbers function and pass the test_numbers list as argument
sorted_test = sort_numbers(test_numbers)

# Verify the output against the expected result
assert sorted_test == test_numbers

```