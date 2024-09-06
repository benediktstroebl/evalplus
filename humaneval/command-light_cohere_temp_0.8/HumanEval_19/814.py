```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    It wanted in a list of strings. It is the splitting on space.) 
    letters are then sorted in ascending order.
    """return "".split(numbers).sort_letters()
    """return "sorted_numbers()")

# Unit tests
numbers = "three one five"
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Output: "one threefive"
numbers = "zero one three"
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Output: "zeroone three"
```