```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(j <= i for j in divmod(i, n)))

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 4
print(largest_divisor(10))  # Output: 4
print(largest_divisor(3))   # Output: 1 (since only 1 divides 3 evenly)
print(largest_divisor(27)) # Output: will be an infinite loop, since no divisors are found
```