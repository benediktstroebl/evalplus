```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating both `x` and `n` as integers, if both evaluations are equal, then it returns `True`, else `False`. Such a check is necessary to ensure that for example `3` is not a simple power of `2` but `3**2` is. 

Here is a simple test suit to check if the function works:
```python
def test_is_simple_power():
    assert is_simple_power(1, 4)
    assert is_simple_power(2, 2)
    assert is_simple_power(8, 2)
    assert not is_simple_power(3, 2)
    assert not is_simple_power(3, 1)
    assert not is_simple_power(5, 3)
```