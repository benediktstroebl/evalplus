```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    :param values: list of any python object
    :return: list of integers
    """
    return [i for i in values if isinstance(i, int)]

# Test the function with a sample values
values_test = [1, 2, 3, 'abc', {}, [1, 2, 3], [3, 2, 1]]
result_test = filter_integers(values_test)
print(result_test)  # Output: [1, 2, 3]

# Another test with list of strings
str_list = ['abc', 'abc123', 'abc@123']
result_str = filter_integers(str_list)
print(result_str)  # Output: []
``` 
This script provides a self-contained function that filters a list of values for only integers. The test cases demonstrate the both the function correctness.