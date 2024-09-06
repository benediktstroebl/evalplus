Here is a Python script that contains a self-contained function that sorts and returns a string of numbers in descending order:
```python
from typing import List

def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of integers.
    Convert to string and sort in descending order
    """
    numbers = [str(num) for num in numbers]
    numbers.sort(reverse=True)
    return numbers
```
This script defines a function `sort_numbers` that takes a list of integers as input and returns a list of strings representing the same numbers, sorted in descending order.