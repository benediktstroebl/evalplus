Here is a self-contained Python script with a function that sorts numbers in a markdown-style input:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_set_ordered_list(numbers).
def make_set_ordered_list(numbers: str) -> List[str]:
    return sorted(numbers.split(" ").  # Splitting numbers into individual strings
     [number.split(" " ")[int(number) - 1]  # Converting to integer and removing separator
     int(sub)  # Converting to integer
     numbers = [sub]  # Converting all numbers to list of strings
     return numbers
```
The code defines two functions, `sort_numbers` and `make_set_ordered_list`. The `sort_numbers` function takes a string of numbers as input, splits it into individual numbers, converts them to integers, and then sorts them in ascending order. The `make_set_ordered_list` function takes a string of numbers as input, splits it into individual numbers, converts them to integers, and returns them as a list of strings, which are then sorted in ascending order.