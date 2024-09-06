```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test cases
values_test = [1, 2, 3, 'abc', int('a'), [], {}]
print("Test case 1: ", end="")
print(filter_integers(values_test))
print("\n")

strings = ['a', 3.14, 5]
print("Test case 2: ", end="")
print(filter_integers(strings))
print("\n")

empty_list = []
print("Test case 3: ", end="")
print(filter_integers(empty_list))
print("\n")

non_integer = "a"
print("Test case 4: ", end=")
print(filter_integers([non_integer]))
print("\n")
```