```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers. If numbers is empty return ""
    if not numbers: return "Input string is empty"
    # remove all non-numeric characters and keep spaces
    numbers = numbers.replace(" ", "")
    numbers = [int(c) for c in numbers if c.isdigit()]
    core_numbers = numbers
    # convert list to set to remove duplicate numbers
    unique_numbers = set(numbers)
    # sort numbers from smallest to largest
    sorted_numbers = list(unique_numbers)
    return "".join(sorted_numbers)

# example usage
numbers = "three one five"
print(sort_numbers(numbers))  # expected output: one three five
```