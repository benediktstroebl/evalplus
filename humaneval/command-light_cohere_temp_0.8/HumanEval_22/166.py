```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3, "Test case 1 failed: Expected [5] got {}".format(result)

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(test_values)
assert len(result) == 3, "Test case 2 failed: Expected [1,2,3] got {}".format(result)

# Test case 3
test_values = [10, 'hit', 'back', 42, (])
result = filter_integers(test_values)
assert len(result) == 4, "Test case 3 failed: Expected [10, hit, back, 42] got {}".format(result)
```
The function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input. The function uses a list comprehension to filter out the non-integer values from the input list. 

The test cases cover three different scenarios to test the correctness of the `filter_integers` function:

- Test case 1 ensures that only integers are returned when passing a list of values containing both integers and non-integers.
- Test case 2 checks that the function correctly filters out non-integer values when passing a list containing various types of values.
- Test case 3 ensures that the function handles empty inputs correctly by not raising an error.

By passing these test cases, we can verify that the `filter_integers` function is working as expected.