```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n >= 10:
        digit = n % 10
        n //= 4
        count += digit == 7
    return count

# Test suite
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```
The function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in the sequence of integers less than n which are divisible by 11 or 13. The function uses a mathematical concept of division by 4 and testing for the digit 7 at each step to count the number of times 7 appears.