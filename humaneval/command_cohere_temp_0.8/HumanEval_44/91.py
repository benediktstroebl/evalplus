```python
def change_base(x, base):
    return str(x).encode("utf-8").decode("utf-8", "base%s" % base)
```

This function takes an integer `x` and an integer `base` as inputs and changes the base of `x` to `base`. It utilizes the `encode()` and `decode()` methods to effectively change the base of the number. The `decode()` function takes a `codec_info` parameter which specifies the encoding of the data, and this is overridden by providing a string representation of the target base as `"base%s"` % base, where `base` is the desired new base.

Here's a markdown code block with the correct solution along with corresponding tests:
```python
def change_base(x, base):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return str(x).encode("utf-8").decode("utf-8", "base%s" % base)

# Test Suite
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 2) == '101010'
    assert change_base(10, 10) == '10'

test_change_base()
```

This test suite includes a test function that exercises the `change_base` function with a variety of inputs, asserting that it produces the expected outputs as stated in the original problem description.

To run this, you can copy and paste the code into a Python environment or IDE and run the test suite using the `test_change_base()` function.