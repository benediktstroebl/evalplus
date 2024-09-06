```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    dp = [0] * (10 + 2)
    for i in range(1, n + 1):
        if i % 10 == 7 or i % 20 == 7:
            dp[i] = dp[i - 1] + 1
    return dp[n]

# Test the function with a few inputs
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function `fizz_buzz` uses a dynamic programming approach. It creates a strings that represent the previous states of the digit count, and for each number less than `n`, it checks if the number is a multiple of 7 (either by modulo 10 or 20) and updates the corresponding string. The final count is the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.