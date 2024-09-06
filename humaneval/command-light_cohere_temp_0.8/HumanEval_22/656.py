```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases for function
test_filter = []
test_filter.push_one = [1, 2, 3, 'abc', 5, 6, 7]
test_filter.push_one_str = ['a', 3.14, 5]
test_filter.push_none = [1, 2, 3, 'def', {}]
test_filter.push_list = [1, 2, 3, ['abc', 'def'], [7, 8, 9]]

# Function Call and Test Results
print(filter_integers(test_push_one))
print(filter_integers(test_push_one_str))
print(filter_integers(test_push_none))
print(filter_integers(test_push_list))

``` 
This script defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. The function uses the Python's `isinstance` built-in function to check if each element in the input list is an integer. 

The script also includes a series of test cases that are passed to the `filter_integers` function to test its functionality. The output of the function call with each test case is then printed to the console to verify the expected results.