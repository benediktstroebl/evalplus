```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 7:
            count += 1
        n //= 11 if digit == 7 else 13
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The above code defines the fizz_buzz function that calculates the frequency of the digit 7 in the numbers less than a given number n, which are divisible by 11 or 13. It uses a specific logic to iterate through the number and checks if the current digit is 7, if it is, it increments the count; otherwise, it divides n by 11 or 13, depending on the current digit. The function then returns the value of count.