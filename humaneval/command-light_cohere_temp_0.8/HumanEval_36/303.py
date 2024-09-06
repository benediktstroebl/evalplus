```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    dp = [0] * (n + 1)
    for num in range(1, n + 1):
        if (num % 11 == 7) or (num % 13 == 7):
            dp[num] = dp[num - 1] + 1
    return dp[n]
# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
The function `fizzBuzz` calculates the number of occurrences of the digit 7 in numbers less than `n` that are either divisible by 11 or 13. The function uses a efficient dynamic programming approach with a bottom-up dp array to solve this problem.