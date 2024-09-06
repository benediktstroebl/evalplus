```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test case 1: Filter integers from a list of values
test_case_1 = ['a', 3.14, 5]
result_case_1 = filter_integers(test_case_1)
assert result_case_1 == [5]

# Test case 2: Filter integers from a list of mixed data types
test_case_2 = [1, 2, 3, 'abc', {}, []]
result_case_2 = filter_integers(test_case_2)
assert result_case_2 == [1, 2, 3]

# Test case 3: Filter empty list
test_case_3 = []
result_case_3 = filter_integers(test_case_3)
assert result_case_3 == []
``` 
This script defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. It uses the simple list comprehension to achieve this. The function is then tested with three different test cases, passing all the tests with assert statements.