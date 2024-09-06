```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Example usage:
values = [1, 2, 'three', 3.14, 5]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3, 5]

# Test the function with a list of various data types and pass the expected output:
test_values = [1, 2, 'three', 3.14, 5, 'foo', {}]
test_results = filter_integers(test_values)
print(test_results)  # Output: [1, 2, 3, 5]
```
This script defines a function called **filter_integers** that takes a list of values as input and returns a new list containing only the integers from the input list. The function achieves this using a **if** statement to filter the values and returns the resulting list.