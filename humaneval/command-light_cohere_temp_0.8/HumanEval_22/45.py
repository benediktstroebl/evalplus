```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print("Test case 1: ", values_test1)
print("Expected Output: ", filter_integers(values_test1))

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print("Test case 2: ", values_test2)
print("Expected Output: ", filter_integers(values_test2))

# Test case 3
values_test3 = [1, 2, 3]
print("Test case 3: ", values_test3)
print("Expected Output: ", filter_integers(values_test3))
``` 
The function **`filter_integers`** accepts a list of values as input and returns a new list containing only the integers from the original list. The test cases demonstrate the different kinds of lists that the function may be used with, and the function will return the right output for each case.