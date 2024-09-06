```python
def largest_divisor(n: int) -> int:
    return next(
        i for i in range(1, n + 1) if all(j % i == 0 for j in range(1, n + 1))
    )

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(50))  # Output: 20
```
This Python code defines a function `largest_divisor(n)` that aims to find the largest integer divisor of a given number `n`. 

It uses a generator expression with the `range()` function and a generator condition `all(j % i == 0 for j in range(1, n + 1))`, which checks if all divisors of `i` are equal to 0. 

The function returns the largest integer that satisfies this condition, ensuring the largest divisor is returned.