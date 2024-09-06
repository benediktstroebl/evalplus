```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(int(d) == i for i in n % d == 0)))

# Test cases
assert largest_divisor(1) == 1
assert largest_divisor(2) == 2
assert largest_divisor(3) == 3
assert largest_divisor(4) == 4
assert largest_divisor(5) == 5
assert largest_divisor(6) == 6
assert largest_divisor(7) == 7
assert largest_divisor(8) == 8
assert largest_divisor(9) == 9
assert largest_divisor(10) == 10
assert largest_divisor(15) == 5
```