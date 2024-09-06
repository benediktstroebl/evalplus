```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```

The function checks if the number is even, and returns n//2 in that case. If the number is odd, it simply returns n+1.