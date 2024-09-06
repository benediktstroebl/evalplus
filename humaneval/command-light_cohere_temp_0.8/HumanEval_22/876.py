```python
from typing import List
def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function
test_values = [1, 2, 3, 'abc', [], 5]
test_result = filter_integers(test_values)
print(test_result)  # Expected output: [1, 2, 3, 5]
```
This script defines a function `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input list. The function uses a typing feature, which allows for more specific and readable syntax when filtering integers.