```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]
values3 = [1, 2, 3]

print("Test case 1: ", end="")
print(filter_integers(values1))
print("\n")

print("Test case 2: ", end="")
print(filter_integers(values2))
print("\n")

print("Test case 3: ", end="")
print(filter_integers(values3))
print("\n")
```

This script defines a function `filter_integers` that filters a list of values and returns a new list containing only the integers. The function utilizes the value of `isinstance` to check if each value in the list is an integer, and then it iterates through the list, using the `filter` function to extract the integers.