```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test the function
values_test = [1, 2, 3, 'abc', [], 5, 6]
result_test = filter_integers(values_test)
print(result_test)  # Output: [1, 2, 3, 5, 6]

# Another test
values_another = [3.14, 5]
result_another = filter_integers(values_another)
print(result_another)  # Output: [5]
```

The function **filter_integers** takes a list of values as an argument. It uses the filter() function from the list module to filter out non-integer values. It then returns a test for each list separately.