```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    document
    every number, from the smallest to the largest, in descending order.
    """
    sorted_numbers = sorted(numbers)
    return "".join(" ").join(sorted_numbers))

#Test cases
numbers = "three one five"
print(sort_numbers(numbers)) # Output: one three five"

numbers = "two three eight five"
print(sort_numbers(numbers)) # Output: two three eight five"

numbers = "zero one two three four five six seven eight nine"
print(sort_numbers(numbers)) # Output: zero one two three four five six seven eight nine"

numbers = "six three seven eight nine"
print(sort_numbers(numbers)) # Output: six three seven eight nine"
```