```python
from typing import List
def longest(strings: List[str]):
    """ Returns the longest string in a list of strings.
    return the string that is longer than any other in the list, or return None if the list is empty"""
    return max(strings, key=len)
# Test the function with different inputs
# empty list
test_empty = longest []
assert test_empty is None
# list with different lengths
test_list = ["a", "bb", "ccc"]
test_list = longest(test_list)
assert test_list == "ccc"
# list with one string
test_single = ["a"]
test_single = longest(test_single)
assert test_single == "a"
```