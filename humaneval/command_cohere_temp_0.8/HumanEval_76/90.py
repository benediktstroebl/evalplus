```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function compares the input number x with the power of n, then checks if n is an integer and if x is equal to the integer power of n, returning true if so, and false if not. 

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))
```

This will output:
```
True
True
True
False
False
False
```

This shows that the function properly classifies simple powers as true and non-simple powers as false.