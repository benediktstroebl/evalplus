```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function compares the input number x with the result of n ** int(x == n * n) and returns true if they are equal, which indicates that x is a simple power of n. The type(n) is int check ensures that the second argument is an integer. When the power is not an integer, the function returns false, as in the corresponding test cases.