```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test the function with a few examples
values_test = [['a', 3.14, 5], [1, 2, 'abc', }, [], 0]
result_test = filter_integers(values_test)
print(result_test)

```
This script defines a function called `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the input list. The script then provides a test cases to verify the correctness of the function.