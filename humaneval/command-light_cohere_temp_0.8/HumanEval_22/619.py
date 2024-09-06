```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function with various inputs
test_values = [['a', 3.14, 5], [1, 2, 'abc', {}, []]

print("Test 1:")
print(filter_integers(test_values))  # Output: [5]

print("Test 2:")
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]

print("Test 3:")
print(filter_integers([10, 20, 30, 40, 50]  [50]))  # Output: [30, 40, 50]

print("Test 4:")
print(filter_integers([1, 2, 3, 4, 'abc']  [4]))  # Output: []
```