```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of values
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, list), "Invalid return type"
assert len(result1) == 2, "Wrong length for filtered values"
assert all(isinstance(x, int) for x in result1), "Non-integer found"

# Test case 2: Filter integers from a list of mixed data types
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert isinstance(result2, list), "Invalid return type"
assert len(result2) == 3, "Wrong length for filtered values"
assert all(isinstance(x, int) for x in result2), "Non-integer found"
```
This Python script defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input. The function uses a filtering technique, where it iterates through the input list and applies type filtering using the `isinstance` function to identify integers. 

Test case 1 ensures that the function correctly filters integers from a list of values, while test case 2 validates the function's behavior when handling a list of mixed data types. 
By passing these test cases, we can verify the correctness of the `filter_integers` function.