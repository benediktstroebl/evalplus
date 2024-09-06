```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function compares the input number x to the power of n when it is raised to an integer value, it returns true when equal and false in other cases. 

The type comparison ensures that the function handles cases where n is not an integer correctly, returning false instead of raising an error. 

To handle the edge case of when n is not an integer, I have checked if the type of n is int before performing the power operation.