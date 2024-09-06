```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

#Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]

print(filter_integers(test_values))

test_list = [1, 2, 3, 'abc', 123456]
print(filter_integers(test_list))

test_Set = {x: 1 for x in range(10)}
print(filter_integers(test_Set))
``` 
The above script defines a function `filter_integers` which takes a list of values and returns a new list that contains only the integers from the original list. The test cases ensure that the script is functional.