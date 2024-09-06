```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base."""
    # Use string formatting to return string representation of number in specified base.
    return f"{x *{x:>{{base}}}"
    return f"{x:>{base}}" 

def test_change_base():
    """Run function test_change_base."""
    assert change_base(8, 3) == '22', "Failed to convert 8 to base 3."
    assert change_base(5, 4) == '20', "Failed to convert 5 to base 4."
    assert change_base(7, 2) == '111', "Failed to convert 7 to base 2."

if __name__ == "__main__":
    test_change_base()
```
The provided code defines a function `change_base` that converts a number to a given base. It utilizes string formatting to return a formatted string representation of the number in the specified base. The `test_change_base` function contains assertions that check the correctness of the `change_base` function.  The ensures that the function's behavior matches the specified requirements.