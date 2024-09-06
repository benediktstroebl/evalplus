```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = [num for num in values if isinstance(num, int)]
    return filtered_ints

# Test cases
test_values = [1, 2, 3, 'abc', {}, [5], [123, '456']]
test_results = filter_integers(test_values)

print("Test Values:", test_values)
print("Test Results:", test_results)

```

This code defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It uses the type hint to ensure that the elements in the list are of the **int** type, and then it uses the **isinstance** operator to filter the elements correctly. The code also includes test cases to ensure that the function works as expected.