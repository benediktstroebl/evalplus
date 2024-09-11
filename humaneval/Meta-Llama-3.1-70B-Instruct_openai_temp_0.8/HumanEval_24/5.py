```python
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n"""
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```

In this script, the function `largest_divisor` takes an integer `n` as input and starts checking from `n-1` downwards for a number that divides `n` evenly. As soon as it finds such a number, it returns it as the result. The `%` operator is used to calculate the remainder of `n` divided by the current number, and if this remainder is zero, the number is considered a divisor.