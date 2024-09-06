```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), 1)

def divisible(n: int, d: int) -> bool:
    return n % d == 0

if __name__ == "__main__":
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 16
    assert largest_divisor(10) == 1
    assert not largest_divisor(7)  # Should return None or error
```