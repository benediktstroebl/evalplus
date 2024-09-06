```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'a', 3, 'bc', 4]
values2 = [5, 'six', 7]
values3 = [1, 2, 3, 4, 'five', 8, '123']

print("Test Case 1: ", end="")
print(filter_integers(values1))
print("\n")

print("Test Case 2: ", end="")
print(filter_integers(values2))
print("\n")

print("Test Case 3: ", end="")
print(filter_integers(values3))
print("\n")
```

This script provides a function named `filter_integers` that accepts a list of values and returns a new list containing only the integers from the original list. The function uses a filtering mechanism to identify and extract the integer elements. The script also includes a set of test cases, designed to validate the function's behavior, ensuring that the function correctly filters only integers from the given list of values.