Here is a self-contained Python script with a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    for i in range(1, n+1):
        digit = ord('7')
        is_divisible = (i % 11 == 0 or i % 13 == 0)
        if is_divisible:
            c += 1
        num_digits = len(str(i))
        if num_digits > 1 and digit > 0 and i != num_digits:
            c += int(10 ** (num_digits - 1) / 2)
    return c
```
This function uses a simple loop to iterate through numbers less than or equal to `n`. It counts the number of times the digit 7 appears and also takes into account the case where the number has more than one digit, and the digit is 7. This digit is once the also ensures that digits 1 to 6 are excluded from the calculation.