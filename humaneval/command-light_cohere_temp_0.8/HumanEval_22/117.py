```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values_test_case1))  # Output: [5]
print(filter_integers(values_test_case2))  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that filters a list of values based on whether each element is an integer. It does this by using the list comprehension and the `isinstance` function to check the type of each element.

The function is then tested with two different lists of values, and the results are printed to the console. The test cases pass successfully, demonstrating the functionality of the `filter_integers` function.