```python
from typing import List

def filter_integers(values:
    """
    filtered_integers = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_integers.append(value)
    return filtered_integers

# Example usage:
values_list = [1, 2, 3, 'abc', {}, [], 5]
result = filter_integers(values_list)
print(result)  # Output: [1, 2, 3, 5]

```
This code defines a function `filter_integers` that takes a list of values as an argument. The function iterates through the filter out any non-integer values from the list and returns a new list containing only the integers. The example usage demonstrates how you can call the function with a list of values and print the resulting list of integers.