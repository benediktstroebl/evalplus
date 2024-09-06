```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine,
    Valid choices are zero, one, two, three, four, five, six, seven, eight, and nine
    """
    # Discard any non-numeric characters
    numbers = numbers.split()
    Dividing by 2, remove any consecutive numbers (e.  # like "6665" to "65" and "89" to "89"
    numbers = [num for num in numbers if num.isdigit()]
    get rid of any non-numeric characters and spaces
    numbers = ' '.join(numbers)
    numbers = numbers.split()
    Rer removing non-numeric characters and splitting by one
    numbers = [int(num) for num in numbers]
    numbers.sort()
    coressp with the previous test and return the sorted numbers as a string
    return numbers
```