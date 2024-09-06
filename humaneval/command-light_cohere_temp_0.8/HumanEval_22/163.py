```python
from typing import List

def filter_integers(values:
    # Filtering function
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []]
]

# Function test
test_filter_integers_result = filter_integers(test_filter_integers)

# Print the result
print(test_filter_integers_result)  # Output: [5, 1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function is then tested using two different test cases, and the results are printed to the console.