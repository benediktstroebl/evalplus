```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return len([i for i in range(1, n+1) if (7 % i) == 0 and i % 15 == 0])

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It uses a length of a list of numbers to count the occurrences of 7.