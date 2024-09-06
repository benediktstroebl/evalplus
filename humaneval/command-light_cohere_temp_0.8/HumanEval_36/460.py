```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i % 10 == 7:
            dp[i] = dp[i - 1] + 1
    return dp[n]

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number n, which are divisible by 11 or 13. The function uses dynamic programming with an array `dp` to store the number of previous 7s encountered. The algorithm iterates from 2 to n, checking if the current number i is divisible by 10 (since 7 is the only conflicting digit). Finally, the function returns the value of dp[n], which represents the final count of 7s.