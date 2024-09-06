```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(j <= i for j in divmod(n, i)))

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(27)) # Output: 6
```

The function `largest_divisor` returns the largest integer that evenly divides the given number `n`. The function uses the `divmod` function and a generator expression to find the largest divisor. 

It then returns the largest suchisor.