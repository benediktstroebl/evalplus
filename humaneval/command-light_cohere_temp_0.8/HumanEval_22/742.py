```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Example of function test
def test(values):
    result = filter_integers(values)
    assert len(result) == 4  # Assert that the length is 4
    assert all(isinstance(x, int) for x in result)  # Assert that all elements are integers
    assert result == [1, 2, 3, 5]  # Assert specific values are correct
test([1, 2, 3, 'abc', {}, []])
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list that contains only the integers from the input list. The `test` function takes a example list of values and passes it to `filter_integers` function. It then asserts that the expected results are obtained, using the `assert` statement.