```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(" ")
    specific numbers to sort in ascending order."""

    numbers = [int(num) for num in numbers.split()]

    strings = [str.strip(str(x) for x in numbers]

    # convert list of strings to set to remove duplicates
    numbers = set(numbers)

    # convert set of numbers to list
    numbers = list(numbers)

    # sort numbers from smallest to largest
    numbers.sort()

    [ reverse = True
    numbers = sorted(numbers, reverse=reverse)

    return "".join(" ".join(numbers))
```  This code defines a function sort_numbers that sorts a list of numbers, it achieves this by first converting the input string into a list of strings and then converting this list into a set to remove duplicates. Finally, the set is converted back to a list and finally sorted in ascending order.