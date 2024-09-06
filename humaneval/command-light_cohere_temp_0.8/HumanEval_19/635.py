```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers: zero one two three four five six seven eight nine
    """
    #map is a built-in function that returns a new list with items from the original list
    # of input
    choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = numbers.split()
    numbers = list(numbers)
    numbers.sort()
    numbers = sorted(numbers)
    return numbers

# Test the function with a couple of inputs
# Test with correct input
test_cases = [
    "three one five"
    "six four eight nine"
    "zero one two three four five six seven eight nine"
    # Test with invalid input
    "asterix"
]

for case in test_cases:
    actual_numbers = sort_numbers(case)
    assert actual_numbers == case.map(actual_numbers)
    ```