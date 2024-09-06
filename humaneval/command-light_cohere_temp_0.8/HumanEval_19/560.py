```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return f"{numbers sorted from smallest to largest}"

test_sort_numbers = []
test_numbers = "three one five"
test_numbers = "zero seven nine"
test_numbers = "two three eight"

test_sort_numbers.append(test_numbers)
test_sort_numbers.append("Sorted: ")
test_sort_numbers.append(sort_numbers(test_numbers))
test_sort_numbers.append("}")
print("Tests passed!")
```