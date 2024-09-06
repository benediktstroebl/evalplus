Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```

The function `modp` takes two arguments, `n` which is an integer and `p` which is also an integer and returns the result of `(1 << n) % p` which is the remainder of the division of 2^n by p. 

The tests assert the function behaves as expected for a couple of cases. 

Please let me know if you would like me to make any changes or additions to the script.