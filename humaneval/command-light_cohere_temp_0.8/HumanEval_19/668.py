```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(c) for c in numbers.
    return f"{sorted(numbers)}".strip()
numbers_test = [
    "three one five",
    "zero two three four five",
    "one two three four six seven eight nine"
]
sorted_test = sort_numbers(test)
print(sorted_test)
```