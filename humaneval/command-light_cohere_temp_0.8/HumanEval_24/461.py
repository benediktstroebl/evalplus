```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not divmod(d, n).))

def divmod(x, y):
    while y:
        x, y = y, x % y
    return x

# Test the function
n = 15
result = largest_divisor(n)
print(result)
```