```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base B"""
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.
    result = ""
    (str("0" + str(x))[::-1])
    while len(result) < base:
        result += "0"
    return result

def test_change_base():
    base = 10
    x = 8
    expected = "22"
    result = change_base(x, base)
    assert expected == result, f"Expected {expected}, but got {result}"

test_change_base()
```
This script defines a function `change_base` that converts a given number `x` to a specified base `base`. The base can be any number from 2 to 36. The test function tests this base and a number `x`, and then asserts that the result of `change_base` matches the expected output.

The test passes if the function returns the expected string and the assert statement is true.