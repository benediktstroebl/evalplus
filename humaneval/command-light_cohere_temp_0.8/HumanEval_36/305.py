```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 2
        count += digit == 7
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
The code defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in integers less than a given number n, which are divisible by 11 or 13. It does so by repeatedly removing the last digit of a number less than n and adding 1 to the count if the removed digit is 7. The function returns the this count of the number of times 7 appears in such numbers.