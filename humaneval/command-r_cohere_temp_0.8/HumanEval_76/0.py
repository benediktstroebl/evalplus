```python
def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise.
    A simple power has integer exponent.
    """
    return x == n**int(math.log(x, n))

# Additional example tests:
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(8, 2) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(3, 3) == False
assert is_simple_power(16, 4) == True
```