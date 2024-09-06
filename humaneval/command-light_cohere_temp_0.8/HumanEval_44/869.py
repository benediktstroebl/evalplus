```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer input 'x' to base 'base'. 
    The output is a string representing x in the new base.
    """
    return format(x, base)

def test_change_base():
    base = 10
    x = 8
    result = change_base(x, base)
    assert result == '22'
    base = 2
    x = 1000
    result = change_base(x, base)
    assert result == '1000'
    base = 7
    x = 111
    result = change_base(x, base)
    assert result == '111'

change_base.test_change_base()
```
The provided code defines a function `change_base` that converts a given integer `x` to a new base `base`. It also includes a related test function `test_change_base` with a series of test cases to ensure the correctness of the `change_base` function. 
For each test case, it checks if the result of the `change_base` function matches the expected output.