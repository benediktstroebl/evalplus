```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are string with numbers zero to nine.
    Sort and return the Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
    a dry run, split_sorted = numbers.sort()
    dry_sorted
    numbers = [int(num) for num in numbers if num.isdigit()]
    dry_sorted = sorted(numbers)
    return dry_sorted

#Example usage
numbers = 'three one five'
sorted_out = sort_numbers(numbers)
print(sorted_out)
```