```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
 assert largest_divisor(15) == 5
 assert largest_divisor(27) == 3
 assert largest_divisor(9) == 3
 assert largest_divisor(12) == 4
 assert largest_divisor(6) == 2
 assert largest_divisor(48) == 8
 assert largest_divisor(30) == 5
 assert largest_divisor(21) == 3
```