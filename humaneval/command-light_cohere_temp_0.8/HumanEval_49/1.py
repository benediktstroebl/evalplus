```python
def modp(n, p): 
    m = 2 ** n % p
    return m if m!=0 else 1

# Test suite
print(modp(3, 5))   # Output: 3
print(modp(1101, 101)) # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101)) # Output: 1
``` 
This code provides a function `modp` that calculates `2^n % p` and passes all the corresponding tests.  The function is a good candidate for solving the problem.