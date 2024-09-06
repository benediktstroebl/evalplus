```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()

Ensure the string contains only digits from 'zero' to 'nine', and does not contain any other characters.


test_sort_numbers = []
test_numbers = """
three one five
six two three
eight four nine
one seven six"

for num in test_numbers:
    test_sort_numbers.append(sorted(num))

# Output should be: ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
```