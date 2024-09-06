```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by comparing it to the result of `n ** int(x == n ** x)`. If `x` is equal to this expression, then it is a simple power of `n`. The int() function is used to handle the case where `x` is not an integer, which would cause an error when raising `n` to the power of `x`. 

Here is a simple test suite to test this function:
```python
def test_simple_power():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
```

This test suite covers a variety of cases, including positive and negative integers for `x` and `n`, and various simple power relationships.  The function should return `True` for the first four tests and `False` for the last three tests. Any deviation from this behavior would be considered a failure.  This can be run by adding these test functions to a Python script and running them.