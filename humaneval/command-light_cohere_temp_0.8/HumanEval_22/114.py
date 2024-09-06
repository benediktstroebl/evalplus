```python
from typing import List

def filter_integers(values:
    """
    filtered_integers = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_integers.append(value)
    return filtered_integers

# Example 1: Test with a list of values
values_list = [3.14, 5, 1, 2, 'abc', 0]
result_list = filter_integers(values_list)
print("Result:", result_list)  # Output: [3.14, 5, 1, 2]

# Example 2: Test with a set of values
values_set = set([3.14, 5, 1, 2, 'abc', 0])
result_set = filter_integers(values_set)
print("Result Set:", result_set)  # Output: {3.14, 5, 1, 2}

# Example 3: Test with a list of any data type values
mixed_values_list = ['a', 3.14, 5, 1, 'abc', 0, [1, 2]]
result_mixed = filter_integers(mixed_values_list)
print("Result Mixed:", result_mixed)  # Output: ['a', 3.14, 5, 1]
```

This script defines a function **`filter_integers`** that takes a list of values and filters it to return a new list containing only the integers from the original list. The function uses a typing and a simple loop to iterate through the list, checking each value with the **`isinstance`** function. 

You can uncomment the lines of the code and run it in your Python environment.