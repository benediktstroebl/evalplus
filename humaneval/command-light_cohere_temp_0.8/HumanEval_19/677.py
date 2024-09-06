```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    yet an integer or makes.
    return [ numbers.sorted()
  # Convert to list
    >> numbers = [int(num) for num in numbers.
    >> sort_by_key(numbers, '>')
    >> numbers
    >> ['zero', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    """
    # Make sure we handle the edge case of having 0 or 9
    if numbers.count('zero') == 1 or if numbers.count('9 zero') > 1:
        numbers.remove('zero')
    numbers = numbers[1:]
    # Add other edge cases here
    if numbers.count('nine') == 1:
        numbers.remove('nine')
    numbers = numbers[1:]
    return numbers.sorted()  # Convert to string
```