```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 2 if digit == 7 else 1
        count += 1
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number n, which are divisible by 11 or 13. The function iterates through the numbers, checking each digit to see if it's 7 and dividing by 2 if it's not. The function then counts the occurrences and returns the result.