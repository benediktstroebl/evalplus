```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of inputs
values_test = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
test_result = filter_integers(values_test)
print(test_result)

```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the `is string conversion and `isinstance` checks to achieve this.

The test cases are created with a variety of values, and the `filter_integers` function is called with these test cases. The result is then printed to verify the function's correctness.