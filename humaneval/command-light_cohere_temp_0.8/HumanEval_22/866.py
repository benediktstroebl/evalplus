```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Expected Output: [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Expected Output: [1, 2, 3]

# Test case 3
values_test3 = [1, 2, 3, 4, 'five', 6]
print(filter_integers(values_test3))  # Expected Output: [1, 2, 3, 4, 6]
``` 
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the Example for this function to pass.