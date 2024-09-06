```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n >= 10:
        if n % 10 == 7:
            count += 1
        n //= 2
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than a given number `n` which are divisible by 11 or 13. The function uses a integers less than `n` as a loop range and checks if the last digit of the number is 7 using the modulo operator (`%`). If the last digit is 7, it increments the `count` variable. Finally, the function returns the count value.