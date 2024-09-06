```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert len(result_test1) == 3, "Test case 1 failed"

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert len(result_test2) == 3, "Test case 2 failed"

# Test case 3
values_test3 = [object(), None, True, (])
result_test3 = filter_integers(values_test3)
assert len(result_test3) == 0, "Test case 3 failed"
```
This Python script defines a function **filter_integers** that filters a given list of values, returning a new list containing only integers. It also provides three test cases to validate the function, passing different lists of values and verifying that only integers are returned.