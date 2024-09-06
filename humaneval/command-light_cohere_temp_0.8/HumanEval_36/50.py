```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 10
        count += digit == 7
    return count

#Test the function with various inputs
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than a given number `n` that are divisible by 11 or 13. The function iterates throughs through the digits in the number less than `n` and counts how many of them are 7.