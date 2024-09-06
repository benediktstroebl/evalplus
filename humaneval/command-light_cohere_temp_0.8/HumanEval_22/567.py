```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_ints.append(value)
    filtered_ints
    return filtered_ints

# Unit tests
values1 = [1, 'a', 3, 'bc', 5]
values2 = [1, 2, 3, 'abc', [], 6]

print("Values 1:", values1)
print("Filter result 1:", filter_integers(values1))

print("\nValues 2:", values2)
print("Filter result 2:", filter_integers(values2))
```
The function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input. The function is designed to run without any external dependencies and can be easily imported and run anywhere in any environment.