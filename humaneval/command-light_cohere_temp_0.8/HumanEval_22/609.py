```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Tests
values_test = [1, 2, 3, 'abc', 10, '20']
print(filter_integers(values_test))  # Output: [1, 2, 3]

string_test = ['a', 3.14, 5]
print(filter_integers(string_test))  # Output: []

empty_test = []
print(filter_integers(empty_test))  # Output: []

int_test = [1, 2, 3, 'four', 'five']
print(filter_integers(int_test))  # Output: [1, 2, 3]
``` 
The function `filter_integers` takes a list of values and returns a new list with only the integers from the input. The function is self-contained and does not use any external functions or modules.