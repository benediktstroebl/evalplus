```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
values_test = [1, 2, 3, 'abc', {}, [1, 2, 3, 'a']]
test_result = filter_integers(values_test)
assert [x for x in test_result if x == int(x)] == [1, 2, 3]

another_test = [1, 2, 3, 'a', 'bc']
another_test_result = filter_integers(another_test)
assert [x for x in another_test_result if x == int(x)] == [1, 2, 3]
 ```

The code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It is then uses a list comprehension with a condition to filter out non-integer values from the input list. The test cases verify the main functionality of the function, passing all the tests with the expected output.