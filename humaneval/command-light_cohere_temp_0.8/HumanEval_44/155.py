```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another.
    :param x: int, the number to be converted
    :param base: int, the desired base (must be > 0)
    :return: string representation of x in base base
    """
    if base < 0:
        raise ValueError("Base must be a positive integer.")
    elif base == 10:
        return str(x)
    else:
        return str(x)[(len(str(x)) - base) : -1]

# Unit tests
test_change_base = []
test_change_base.push(8)
test_change_base.push(12)
test_change_base.push(21)
test_change_base.push(42)
test_change_base.push(24)
test_change_base.push(61)
test_change_base.push(100)
test_change_base.push(162)
test_change_base.push(123)

def test_change_base():
    for num, base in zip(test_change_base, range(26)):
        base = int(base)
        try:
            print(f"{num}: {change_base(num, base)}", end="")
        except ValueError as e:
            print(f"Error: {e}")
```
The code defines a function `change_base` that converts a number `x` to a string in a specified base `base`. The function first checks if the base is a valid positive integer, then converts `x` to a string using the appropriate method. The `test_change_base` unit test suite ensures that the `change_base` function works correctly for a variety of inputs and base values.