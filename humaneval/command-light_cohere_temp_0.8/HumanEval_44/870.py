```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after conversion.
    base numbers less 10."""
    return str(x, base)

def test_change_base():
    assert change_base(8, 3) == '22', "Failed with 8 and 3"
    assert change_base(5, 2) == '100', "Failed with 5 and 2"
    assert change_base(10, 5) == ' 610 ', "Failed with 10 and 5"

# Use the main function
if __name__ == "__main__":
    test_change_base()
```
This Python script defines a function `change_base` that converts a given number `x` to a specified base `base`. It also includes a function `test_change_base` to run the `change_base` function with various inputs and asserts that the function returns the expected result.  The test_change_base function to ensure its correctness with different inputs.