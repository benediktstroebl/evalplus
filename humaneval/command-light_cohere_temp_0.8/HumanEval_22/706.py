Here is a Python script with a self-contained function that solves the problem of filtering integers from a given list:

```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if x != "" and x.isinstance(int)]
def test_filter_integers(values):
    assert filter_integers(values) == [1, 2, 3]
test_filter_integers(['a', 3.14, 5])
test_filter_integers([1, 2, 3, 'abc', {}, []])
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a list comprehension and the `isinstance()` built-in function to check if each value is an instance of the `int` class. The script also defines a function `test_filter_integers` which takes a list of values and asserts that the `filter_integers` function returns the correct output for the given input.