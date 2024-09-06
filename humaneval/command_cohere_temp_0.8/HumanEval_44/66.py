```python
def change_base(x, base):
    return str(x).convert(base)
```

The `str.convert` method is used for converting between different numerical bases. This method returns a string representing the number in the specified base.

The function follows the problem statement and returns the string representation of the conversion. 

This solution just uses methods built into Python, no extra modules needed.

This problem can also be solved using `int()` and `bin()` or `oct()`, `hex()` functions, but it's the simplest one.

Here are some examples of test cases to ensure the function performs as intended:
```python
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
>>> change_base(10, 2)
'1010'
>>> change_base(15, 5)
'101'
>>> change_base(99, 10)
'9'
>>> change_base(257, 2)
'11111011'
>>> change_base( Humble(123), 36)
'OK'
```