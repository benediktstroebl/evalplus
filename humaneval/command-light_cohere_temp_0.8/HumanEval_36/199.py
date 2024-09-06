```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit[-1] == "7" and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This function, `fizz_buzz`, takes an integer `n` as input and returns the number of times the digit 7 appears in the integers less than `n` that are divisible by 11 or 13. It uses a short loop to iterate through the numbers from 1 to `n`, and checks each number's last digit to see if it is 7. If the digit is 7 and the number is either odd-numbered or is divisible by 13, the count is incremented.