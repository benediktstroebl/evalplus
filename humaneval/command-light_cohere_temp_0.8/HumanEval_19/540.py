```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.group(sorted(numbers.split(" "))
```

This code defines a function called sort_numbers that takes a string of numbers separated by spaces as input and returns the string with the numbers sorted from smallest to largest. The function uses the group() function with the sorted() method from the string to split the numbers into a list, and then sorts the list. This provides a test solution to the given problem.