Here's a self-contained Python script with a function that filters out integers from a list of various types:
```python
from typing import List, Any

def filter_integers(values:
    # Filtering integers from the given list of any values
    filtered_ints = [x for x in values if isinstance(x, int)]
    return filtered_ints

# Unit tests
def test_filter_integers():
    test_list = [1, 'a', 3.14, 5]
    expected = [5]
    got = filter_integers(test_list)
    assert expected == got

# Example usage
test_filter_integers()
```
This script contains a function `filter_integers` that accepts a list of values and returns a new list containing only the integers from the input. Additionally, it has unit tests and an example usage to show how the function works.

Note: You can add more tests and use this script in your project to filter integers in lists of various data types.