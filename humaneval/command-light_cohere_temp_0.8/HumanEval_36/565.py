```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-prefix="0123456789abcdefghijklmnopqr",]
        while digit == "7":
            digit = str(i)[::-1]
            count += 1
            if int(digit) <= 9:
                break

    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function `fizz_buzz` returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.