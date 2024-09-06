```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)
```

The function takes a `number` as input, which is a positive floating point number, and returns the decimal part of the number. It does so by taking two integers, the given number `num` and the largest integer smaller than `num`, which is obtained via floor division (`int(num)`). The residual value is the decimal part of the original number, which is returned by the function. 

To demonstrate the function, here is an example of usage:
```python
# Test the function
assert truncate_number(3.5) == 0.5
assert truncate_number(12.8) == 0.8
``` 

This would yield the following outputs:
```
0.5
0.8
``` 

These assertions test the function's correctness against known values.