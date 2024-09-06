```python
from typing import List

def filter_integers(values:
    """
        filtered = [int(item) for item in values if item.isdigit()]
        filter_integers(values)
    return filtered

# Test case 1: Filter integers from a list of strings
test_case_1 = [3.14, 'a', 5]
result_test_case_1 = filter_integers(test_case_1)
assert result_test_case_1 == [5]

# Test case 2: Filter integers from a list of other data types
test_case_2 = [1, 2, 3, 'abc', {}, []]
result_test_case_2 = filter_integers(test_case_2)
assert result_test_case_2 == [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the input. The function uses a list comprehension to filter out the integers from the input. 

The script also provides two test cases to verify the correctness of the function. The first test case passes the filter integers from a list of strings, and the second test case passes integers from a list of other data types.