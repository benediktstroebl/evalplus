```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test case 1
test_values1 = ['a', 3.14, 5]
result1 = filter_integers(test_values1)
assert result1 == [5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(test_values2)
assert result2 == [1, 2, 3]
```
This Python script defines a function **filter_integers** that filters a list of values for only integers. It takes values passed as an argument to the function and returns a new list with only the integers present in the original list.