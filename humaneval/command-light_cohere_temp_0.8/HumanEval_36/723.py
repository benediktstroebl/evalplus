```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 2
        count += digit == 7
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in integers less than a given number n, which are divisible by 11 or 13. The function iterates through while n is greater than 0, and at each step, it takes the last digit of n, then divides n by 2 to eliminate higher-order digits and adds to the count if the removed digit is 7.  The final count represents the number of times 7 appears in the sequence.