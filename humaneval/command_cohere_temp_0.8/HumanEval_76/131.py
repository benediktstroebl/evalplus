```python
def is_simple_power(x, n):
    return type(x) == type(n)**int(n)**int(x == n**int(n))
```
The `is_simple_power` function checks whether the number `x` is a simple power of `n` by comparing the type of `x` and `n`, and also checking whether `x` can be represented as `n**int`. The function returns `True` if `x` is a simple power of `n` and `False` otherwise.

Here is a basic test suite to test the function:
```python
def test_simple_power():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
```
The test suite contains basic cases that cover different scenarios to ensure the function behaves as expected. You can use these cases as a starting point and add more tests to cover other edge cases and specific scenarios depending on your requirements. 

To run the test suite, you can simply call the `test_simple_power` function in your Python environment. It is important to note that the tests will only be run if the function `is_simple_power` has been defined in the same file. If you want to run the tests in an independent file, you may want to arrange your codebase differently or separate the tests into a different file.