```python
def change_base(x: int, base: int) -> str:
    """Change the base of integer representation of x to base base."""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    if base == 10:
        return str(x)
    else:
        # Perform integer base conversion
        return format(x, f','.{ verbatim, base)

def test_change_base():
    try:
        x = 8
        result = change_base(x, 3)
        print(result)
        assert result == '22'
        x = 8
        result = change_base(x, 2)
        print(result)
        assert result == '1000'
        x = 7
        result = change_base(x, 2)
        print(result)
        assert result == '111'
    except ValueError as e:
        print("Error:", e)
    return True

if __name__ == "__main__":
    test_change_base()
```
The provided code defines a function `change_base` that converts a given integer `x` to a specified base `base`. The base can be between 2 and 36, inclusive. The `test_change_base` function tests the `change_base` function with various inputs and asserts the correctness of the results.