```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values1 = ['a', 3.14, 5]
print(filter_integers(test_values1))  # Expected output: [5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(test_values2))  # Expected output: [1, 2, 3]

# Test case 3
test_empty_values = []
print(filter_integers(test_empty_values))  # Expected output: []
```

The function **filter_integers** takes a list of values as an argument and returns a new list containing only the integers from the original list. The test cases demonstrate how the Python is an interpreted language that supports dynamic typing and user-friendly function definitions, which means that you can create new functions and variables without explicitly declaring them.