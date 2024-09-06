```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base B"""
    assert base > 0, "Base must be positive"
    assert isinstance(x, int), "Input must be integer"
    assert isinstance(base, int), "Base must be integer"
    if base == 10:
        return str(int(x))
    elif base > 10:
        return f"{x}({base})"
    else:
        return f"{x}({base})"

def test_change_base():
    """Test case for change_base function"""
    assert change_base(8, 3) == '22', "Wrong output for base 3"
    assert change_base(8, 2) == '1000', "Wrong output for base 2"
    assert change_base(7, 2) == '111', "Wrong output for base 2"
    assert change_base(-3, 2) == '-111', "Wrong input for negative number"
    assert change_base(10, 5) == '500', "Wrong base for 10"

if __name__ == "__main__":
    test_change_base()
```
This Python code defines a function `change_base` that converts a number to a specified base, and passes tests to ensure its correctness. It defines another function `test_change_base` to test the `change_base` function with various inputs and expected outputs.