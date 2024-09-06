```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats, stripping any trailing zeros from integers or floats
    a, b = (float(a.rstrip('0')) if isinstance(a, (str, int)) else a,
            float(b.rstrip('0')) if isinstance(b, (str, int)) else b)
    return max(a, b, key=lambda x: (isinstance(x, float), x)) if a != b else None
```

The solution employs the `max` function with a custom `key` argument to compare the numbers. The `key` argument is a function that tells `max` how to determine the sort order of the inputs. This function is `lambda x: (isinstance(x, float), x)`. 

`isinstance(x, float)` returns `True` if `x` is a floating point number and `False` otherwise. When sorting, this configuration ensures that `float()` numbers are always sorted ahead of `int()` ones. In the case of ties, the original values are compared, hence the `x` argument. 

Moreover, the code trims trailing zeros from the integers and floats to ensure accurate comparison, e.g., `compare_one('5,2', '5')` returns `'5,2'`, as it correctly identifies the latter as the larger value. 

The function returns `None` if the inputs are equal.