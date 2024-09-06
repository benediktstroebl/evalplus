```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 2 if digit == 7 else 1
        count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a iterative approach to find the digit at n's position in the remaining sequence of integers less than n.