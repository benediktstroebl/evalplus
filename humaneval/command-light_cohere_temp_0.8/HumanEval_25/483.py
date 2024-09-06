```python
def factorize(n): 
    factors = []
    while n > 1: 
        d = n // gcd(n) 
        factors.append(d)
        n = n - d
    factors.append(n)
    return factors

def gcd(x, y): 
    while y: 
        x, y = y, x % y
    return x

# Run function test
test_factorize = []
test_factorize.py = [int](n) for n in [8, 25, 70, 1337, 2, 63937, 2837844])
print("Prime factors for", py)
print(factorize(py))
```