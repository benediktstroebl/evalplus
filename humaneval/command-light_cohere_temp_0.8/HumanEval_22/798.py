```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case: Filter out integers from a list with mixed data
values_test = [1, 2, 'three', three, 4, 'five', True, 6]
result_test = filter_integers(values_test)
assert isinstance(result_test, list), "Filter returned non-list"
assert len(result_test) == 6, "Filter did not return correct number of items"

# Another test case: Filter integers from a string
string_test = "abcde12345"
result_string_test = filter_integers(string_test)
assert isinstance(result_string_test, list), "Filter returned non-list"
assert len(result_string_test) == 0, "Filter returned non-zero length"
``` 
This script defines a function **filter_integers** that accepts a list of values and returns a new list that contains only the integers from that input. This script then includes two test cases to verify the functionality of the function.