```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test = [
    [1, 2, 3, 'abc', },
    [],
    [5],
]

print(filter_integers(values_test))  # [[1, 2, 3], [], 5]

empty_list_test = []
print(filter_integers(empty_list_test))  # []

string_test = "string"
print(filter_integers(string_test))  # []
```

This script defines a function called `filter_integers` that filters a list of any values, returning only the integers. It uses a filtering is achieved through the use of the Python list comprehension with the `type` check. The test cases cover various scenarios to ensure the function's correctness.