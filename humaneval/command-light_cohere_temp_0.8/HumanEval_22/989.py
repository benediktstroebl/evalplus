Here is a self-contained Python script with a function that filters integers from a given list:
```python
from typing import List

def filter_integers(values:
    # Filter the list for integers
    result = [x for x in values if type(x) == int]
    return result

# Test the function with different data types
test_data = [1, 2, 'three', 3.14, (5)]
result = filter_integers(test_data)
assert result == [1, 2, 3]

# Test with nested data types
test_nested = [1, 2, {'a': 3, 'b': 'hello'}]
result_nested = filter_integers(test_nested)
assert result_nested == [1, 2]

# Test with custom data type
test_list = [list(map(int, 'abc'))]
result_list = filter_integers(test_list)
assert result_list == []

# Test with zero elements
test_empty = []
result_empty = filter_integers(test_empty)
assert result_empty == []
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the original list. It is also provides several tests to validate the correctness of the function with various inputs, such as lists, nested dictionaries, and custom data types. 

This script is designed to be fully self-contained, and does not require any external dependencies or additional functions for testing.