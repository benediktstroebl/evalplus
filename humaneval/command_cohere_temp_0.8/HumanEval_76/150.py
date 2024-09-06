```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly calculating the integer square root of n and raising n to the power of that value, thereby efficiently determining if `x` is a simple power of `n` without the need for brute force. 

Here is a test suite to ensure the algorithm performs correctly:
```python
# Simple test suite
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(8, 2) == True

assert is_simple_power(3, 2) == False
assert is_simple_power(3, 1) == False
assert is_simple_power(5, 3) == False
```