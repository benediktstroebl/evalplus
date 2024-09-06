```python
from typing import List

def filter_integers(values):
    return [int(element) for element in values if element.isinstance(int)]

# Test cases for function evaluation:
test_values = [
    ['a', 3.14, 5],  # contains non-integer elements
    1, 2, 3, 'abc', [], {}  # contains mixed data types

if not test_values == filter_integers(test_values):
    print("Function passed all tests!")
else:
    print("Function did not pass all tests.")
```