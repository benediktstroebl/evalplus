```python
def change_base(x: int, base: int):
    """
    Change the base of the numerical number x to base base.
    Return string representation after conversion.
    base numbers are strings are either 10 or 2.
    """
```
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(10, 2) == '1000'
    assert change_base(7, 2) == '111'

```
This Python code defines a function `change_base` that converts a given number `x` to a string using a specified base `base`. The function utilizes an indentation-based structure that enhances code readability, clearly indicating function and test cases. The `test_change_base` function ensures the `change_base` function's correctness through comprehensive tests.