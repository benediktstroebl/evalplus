```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 3, 'abc', 3.14, 5]
expected_result = [1, 2, 3]
result = filter_integers(values_test)
assert result == expected_result

another_test = [1, 2, 3, 'b', {}]
result_another = filter_integers(another_test)
assert result_another == [1, 2, 3]
```
This code defines a function `filter_integers` that filters a list of any values and returns a new list containing only the integers. 

The function is tested using two different cases:
1. The first test case is designed to test if the function correctly filters only the integers from a given list. The function is expected to return `[1, 2, 3]` as the result.
2. The second test case is designed to test the function with a different list of values, which includes integers and non-integers. The function is expected to return `[1, 2, 3]` as the result again.