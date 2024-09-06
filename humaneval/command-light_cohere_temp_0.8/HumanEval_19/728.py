```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are standard integers, except 'zero'
    Return the string with numbers sorted from smallest to largest.
    """
    list to string conversion takes place.
    numbers = [list of(filter(str.isdigit, numbers.
    sorted(numbers) 
    return ' '.join(sorted(numbers))

numbers = ['three one five', 'two three four', 'eight seven eight']
print(sort_numbers(numbers))
```