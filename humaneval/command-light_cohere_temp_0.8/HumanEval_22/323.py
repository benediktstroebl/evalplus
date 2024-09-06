```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]
):
    pass

# Test cases for function
values_test = [ 
    ['a', 3, 14, 5, 1, 2, 3, 'abc', {}, []]
)
result = filter_integers(values_test)
assert len(result) == 6, "Function did not return expected result"
assert all(isinstance(x, int) for x in result), "Function returned non-integers"
```

This script defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. The function uses a `isinstance` function to check if each element in the input list is an instance of the `int` class. The test cases are used to verify the correctness of the function by passing the test list and checking if the returned result is as expected.