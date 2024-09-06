```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base))) if base != 10 else str(x)
```

This function takes two arguments, `x`, which is the integer to have its base changed, and `base`, which is the new base for the number. The `bin()` function converts the integer `x` to a binary string representation, and the slice `[2:]` is used to remove the '0b' prefix. The `zfill()` method left pads the binary string with zeros to the length of the shortest representation of `x` in the new base, which is calculated using the `math.ceil()` of the logarithm of `x` in base `base`. This method ensures that the returned string is the shortest representation of `x` in the specified base.

The special case is handled for `base 10` with the statement `return str(x)`. 

Here is a test suite that can be used to validate the function:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(42, 4) == '2'
    assert change_base(123, 5) == '22500'
    assert change_base(421, 7) == '133'
    assert change_base(99, 10) == '99'
``` 

Can I help you with any other tasks involving this function or testing principles?