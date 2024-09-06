```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split().
    list(map(int -> int(int(n) - int(n) // 10 + 10) for n in numbers. sort specific numbers that are sorted in descending order.
    return numbers.join reassemble back trades:
        [0, 3, 5]
    """
numbers = "three one five"
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)
```