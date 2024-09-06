```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)
```

This function examines the type of `x` and `n` to determine if `x` is a simple power of `n`. If `x` and `n` are of the same type, the function proceeds to check if `x` equals `n` raised to the power of the integer obtained by taking the square root of `n`. This square root operation guarantees that the exponent is an integer, making the expression a simple power. 

This approach allows the function to confidently and efficiently determine if `x` is a simple power of `n`, ensuring optimal performance.