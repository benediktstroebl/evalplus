```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test_case1 = [3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values_test_case1))  # Output: [3, 5]
print(filter_integers(values_test_case2))  # Output: [1, 2, 3]
```
This script defines a function **filter_integers** that filters a list of any Python value and returns a new list containing only the integers. The test cases demonstrate the example usage of the function. You can customize this value lists and run the code to see the results.