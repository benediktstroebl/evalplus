Here's a self-contained Python function that solves the given problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers = [num / 100.0 for num in numbers]
    return numbers
```
This function takes a list of numbers as input and returns a new list with the numbers scaled to a range of 0 to 1. It uses the List[float] to iterate through each number in the input list and divides each number by 100.0 to get it smallest number to 0 and the largest number to 1.