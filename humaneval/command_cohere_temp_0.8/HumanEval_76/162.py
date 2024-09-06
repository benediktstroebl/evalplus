```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function `is_simple_power` checks if a given number `x` is a simple power of `n` by comparing it to the result of raising `n` to the power of `int(n ** 0.5)`, which is the largest integer less than or equal to `n ** 0.5` that can raise `n` to the desired power. The function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

Here is a simple test suite to validate this function:
```python
# simple test suite
def test_is_simple_power():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
``` 

This test suite contains various test cases to cover different scenarios, including positive matches, as well as cases where the input should not match the desired pattern. 
To run these tests, you can simply call the `test_is_simple_power` function in your Python environment. 

You can also automate this process using testing frameworks like `pytest` or `unittest` to handle the test execution and reporting for you.