```python
def largest_divisor(n: int) -> int:
    return n if n > 1 else 1
    return n  # single-digit numbers have only 1 as a divisor

# Test cases
assertEqual(largest_divisor(1), 1)
assertEqual(largest_divisor(2), 2)
assertEqual(largest_divisor(3), 3)
assertEqual(largest_divisor(4), 4)
assertEqual(largest_divisor(5), 5)
assertEqual(largest_divisor(6), 6)
assertEqual(largest_divisor(7), 7)
assertEqual(largest_divisor(8), 8)
assertEqual(largest_divisor(9), 9)
assertEqual(largest_divisor(10), 10)

# Check for negative numbers
assertEqual(largest_divisor(-1), 1)
assertEqual(largest_divisor(-2), 1)
assertEqual(largest_divisor(-3), 1)
```
The above Python script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. The function returns `n` if `n` is greater than 1, otherwise returns `1` as the largest divisor of `n`, ensuring the function's correctness and efficiency.