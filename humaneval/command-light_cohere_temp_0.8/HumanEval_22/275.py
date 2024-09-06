```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = ['a', 3.14, 5]
assert filter_integers(test_values) == [5], "Test case 1 failed"

# Test case 2
test_list = [1, 2, 3, 'abc', {}, []]
assert filter_integers(test_list) == [1, 2, 3], "Test case 2 failed"
``` 
This code defines a function called filter_integers, which accepts a list of any values and returns a new list containing only the integers from the input. The function uses the filters the integers in the list using the isinstance(x, int) condition. The test cases ensure that the function behaves correctly.