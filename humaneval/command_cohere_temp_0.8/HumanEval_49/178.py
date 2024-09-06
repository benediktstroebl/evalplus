```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` is defined to solve the problem of computing `2^n % p` where it returns the result of `2^n % p` after taking two arguments `n` and `p` respectively. It uses the built-in Python function `pow()` to calculate the power of `2` and then calculates the modulo `%` with respect to `p` which ensures the result is wrapped between the range of `0%p` to `((p-1)%p)` as the latter is usually desired when dealing with cryptography or error correction scenarios especially when `p` is a prime number. 

The tests are correct and show the correct behavior of the function against the problem statement.
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```

Also, the function is concise and is only one line long which is a nice characteristic for a function in a production environment. 

Please let me know if you would like to have any other adjustments or additions to this script.