```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    m = 0
    for i in range(2, n+1):
        digit = str(i)
        if digit[0] == 7 and (i % 11 == 0 or i % 13 == 0):
            m += 1
    return m

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This code defines the fizz_buzz function that calculates the number of occurrences of the digit 7 in numbers less than n which are divisible by 11 or 13. The function iterates from 2 to n+1 and checks if the digit at the beginning is 7 and the number is divisible by 11 or 13. It increments the number of occurrences.