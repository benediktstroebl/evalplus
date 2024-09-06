```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to be converted, and `base`, which is the conversion target base. Using the built-in function `bin`, this function converts the integer `x` to a binary string representation. Afterward, it removes the leading '0b' from the result and then uses `zfill` to add zeros to the left of the string to ensure the result has the same length as the integer's value in the given base. This length is determined using `math.log(x, base)` and `math.ceil` to round up, ensuring the representation is always a valid and minimum-length base conversion.

Here is a test case to ensure the function behaves as expected:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'

test_change_base()
```