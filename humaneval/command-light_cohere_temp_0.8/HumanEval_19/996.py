Here is a self-contained Python script that solves the problem of sorting numbers in Markdown code blocks:
```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest
    Return the string with numbers sorted.
    """
    specific, numbers, and returns a sorted string.
numbers = "three one five"
sorted_string = sort_numbers(numbers)
print(sorted_string)  # Output: "one threefive"
```
This script defines a function `sort_numbers` that sorts a given string of numbers in Markdown code blocks from smallest to largest values.