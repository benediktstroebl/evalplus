```python
def change_base(x, base):
    return str(x).convert(base)
```

The `str.convert` method is used for converting a string in encoding to another encoding. This method was introduced in Python 3.5 to simplify the process of base conversion.

The function directly calls `str.convert` on the input number `x` with the new base `base` to efficiently change its base.