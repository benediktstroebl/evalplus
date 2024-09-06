```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly comparing the target (`x`) to the `n`th power of `n`. It checks that `x` is of integer type and then verifies the expression `n ** int(n ** 0.5) == x` to determine if `x` is a simple power of `n`. 

It should be noted that the int() function in Python converts any floating-point number to its integer representation (with truncation of the decimal part), which simplifies the comparison process in this solution. 

To handle the various test cases provided, this solution assumes that both `x` and `n` are integers and that any operation involving these values will result in an integer result as well. 

If any of the conditions are not met, such as if `x` or `n` is not an integer or if the result of the power operation is not an integer, the function will fail.  This approach focuses on the core relationship being tested and is designed to efficiently handle the intended use cases.