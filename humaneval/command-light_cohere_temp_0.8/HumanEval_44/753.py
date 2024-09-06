```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 not supported.
    """
    base must be either 10 or 32
    """
    if base < 2 or base > 32:
        raise ValueError("Base must be between 2 and 32.")
    return f"{x:>{base}b"

def test_change_base():
    base = 10
    x = 8
    result = change_base(x, base)
    assert result == "22"

    base = 32
    x = 8
    result = change_base(x, base)
    assert result == "1000"

    base = 2
    x = 7
    with pytest.raises("Cannot convert 7 to base 2"):
        result = change_base(x, base)

test_change_base()
```
This Python script defines the function `change_base` that converts a given number to a specific base. The `test_change_base` function provides test cases to ensure the correctness of the `change_base` function. 

Finally, the `pytest` module is used for testing and assertion checking.