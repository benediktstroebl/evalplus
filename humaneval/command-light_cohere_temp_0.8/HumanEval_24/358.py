```python
def largest_divisor(n: int) -> int:
    return n if n == 1 else largest_divisor(n // 2)

# Test cases
assert largest_divisor(1) == 1
assert largest_divisor(2) == 2
assert largest_divisor(3) == 3
assert largest_divisor(4) == 4
assert largest_divisor(5) == 5
assert largest_divisor(6) == 6
assert largest_divisor(7) == 24
assert largest_divisor(8) == 64
assert largest_divisor(9) == 144
assert largest_divisor(10) == 120
assert largest_divisor(11) == 340
assert largest_divisor(12) == 432
assert largest_divisor(13) == 1296
assert largest_divisor(14) == 2304
assert largest_divisor(15) == 2304
```