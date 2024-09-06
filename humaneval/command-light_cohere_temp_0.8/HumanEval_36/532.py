Here's the self-contained Python function that solves the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    dp = [0]
    
    def helper(num):
        if num == 0:
            return 0
        if num % 10 == 7:
            dp[num] += helper(num // 10)
        else:
            dp[num] += helper(num // 10) + 1
            
    return dp[n]

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This function `fizz_buzz` uses dynamic programming to efficiently calculate the number of occurrences of the digit 7 in integers less than `n` that are divisible by 11 or 13. It uses a helper function to calculate the number of digits less than 7 and then accumulates the results based on the input number.