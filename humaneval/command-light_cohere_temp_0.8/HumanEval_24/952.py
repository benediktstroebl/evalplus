```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not divmod(n, d). return(0)))

def divmod(x, y):
    if y == 0:
        return x
    a, b = x, y
    while b:
        a, b = b, a%b
    return a

def test_largest_divisor():
    assert largest_divisor(15) == 5
```