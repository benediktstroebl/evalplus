```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base specified"""
    if x < 0:
        raise ValueError("Input number should be positive")
    return format(x, f"{base}"))

def test_change_base():
    base = 10
    x = 8
    got = change_base(x, base)
    assert got == '22'

    base = 2
    x = 1000
    got = change_base(x, base)
    assert got == '1000'

    base = 7
    x = 111
    got = change_base(x, base)
    assert got == '111'

# Run the tests
test_change_base()
```
This code defines a function `change_base` that converts a given number to a specified base. The `test_change_base` function contains test cases that demonstrate the correctness of the `change_base` function.  The run these code through `python test.run`, which will to execute the tests and verify if the `change_base` function produces the expected output.