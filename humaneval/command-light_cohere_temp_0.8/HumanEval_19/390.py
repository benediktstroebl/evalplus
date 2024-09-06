```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # your code here
    return f"{numbers[0]}{numbers[1]}{numbers[2]}..."

# Test cases
test_cases = [
    "three one five",
    "six four three",
    "zero nine eight seven six",
    "one two three four five six"
]

for test in test_cases:
    actual = sort_numbers(test)
    assert actual == f"{test[1]}{test[2]}{test[3]}", f"Test {test} failed"

print("All tests passed!")
```