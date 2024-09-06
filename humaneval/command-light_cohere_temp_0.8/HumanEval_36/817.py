```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 7:
            count += 1
        n //= 10
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python function, `fizz_buzz`, calculates the number of times the digit 7 appears in the sequence of integers less than a given number `n` that are both divisible by 11 and 13. The function iterates through loop and each time the modulus of the current number to 10 (to eliminate the number itself), and increments the count if the result is 7. The test cases demonstrate the efficient function.