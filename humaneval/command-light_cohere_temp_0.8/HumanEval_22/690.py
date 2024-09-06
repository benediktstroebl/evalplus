Here is a self-contained Python function that solves the problem of filtering integers from a list:
```python
def filter_integers(values):
    return [int(item) for item in values if item.isdigit()]
```

def test_filter_integers():
    values = [1, 2, 3, 'abc', {}, [], 5]
    result = filter_integers(values)
    assert result == [1, 2, 3, 5]
```

This function, `filter_integers`, takes a list of values as input and returns a new list containing only the integers from the original list. It uses Python's string conversion to check if each element is a digit, and then converts it to an integer using the int() function. 

The function is then tested using the `test_filter_integers` function, which creates a list of values and passes it to the `filter_integers` function.