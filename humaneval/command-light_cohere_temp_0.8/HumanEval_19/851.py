```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are method handles invalid inputs.
    Converts the class string of numbers to a list, then sorts it.
    Return the string with numbers sorted from smallest to largest
    """
    #type checking
    assert isinstance(numbers, str), 'Input must be a string of numbers'
    #valid choices method handles invalid inputs
    assert numbers.split(' ', ') == ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 'Invalid input: must contain "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine".
    return numbers.sort()
stricks_numbers_test(numbers)

def sort_numbers_test(numbers: str) -> None:
    #Pass the test by returning an empty string.
    return numbers.split(' ', ')[0]
```