```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test cases
test_filter_integers = [
    [['a', 3.14, 5], [1, 2, 'abc', {}, []], [1, 2, 3, 'a', [4, 5]]],
    [List([1, 2, 3]), List([])]
]

for test in test_filter_integers:
    actual = filter_integers(test)
    assert actual == [num for num in test if isinstance(num, int)], "Test failed: " + str(test) + " failed"
``` 
This script defines a function called `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the input list. The function works by using a `isinstance` function to check if each value in the input list is an integer, and then uses the filter function to create a new list that only contains the integers. 
This script also includes several test cases that can be used to test the `filter_integers` function.