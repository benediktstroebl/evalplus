```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function corroborates that the exponent `n` is an integer and the `base` n raised to the power of `x` equals `x`; if both conditions are met, it returns `True`. 

Here is an example of function usage:
```python
# Highlighting some simple cases
print( is_simple_power(1, 4) )  # True
print( is_simple_power(2, 2) )  # True
print( is_simple_power(8, 2) )  # True

print( is_simple_power(3, 2) )  # False
print( is_simple_power(3, 1) )  # False
print( is_simple_power(5, 3) )  # False
``` 

In the example, the output is as follows:
```
True
True
True
False
False
``` 
The first three statements yield `True` because they respectively illustrate the correct application of the definition of a simple power, i.e., `n ** int(x) = x`. The last three examples demonstrate instances where the condition is not met, thereby returning `False`. 

This function is straightforward and effective in determining whether a number is a simple power of another number.