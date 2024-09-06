```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        odd = tri(n - 1) + tri(n - 2) + tri(n + 1)
        even = 1 + n // 2
        return odd if n % 2 == 0 else [even] + odd
```