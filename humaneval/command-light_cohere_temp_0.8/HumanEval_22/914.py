Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
test_values = [1, 2, 3, 'abc', 4, 5, (6)]
test_cases = [filter_integers(values) for values in test_values]

print("Test Cases:", test_cases)

# Correct Output: [1, 2, 3, 4, 5]
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses a filtering and type checking to achieve this.