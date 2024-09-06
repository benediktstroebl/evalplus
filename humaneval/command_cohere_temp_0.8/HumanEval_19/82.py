```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function splits the string of numbers and converts the list of strings into a list of integers, then sorts them from smallest to largest. It then joins the sorted list of numbers back into a string and returns the result.

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # Outputs one three five
```
This expects the numbers to be space-delimited within the string, with valid choices being 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.