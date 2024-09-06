Here's the Python script with the self-contained function:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-formatrepr(int)]
        if digit == '7':
            count += 1
        if count == 1 and i % 11 == 0 or i % 13 == 0:
            count = 0
    return count

#Test the function
 assert fizz_buzz(50) == 0
 assert fizz_buzz(78) == 2
 assert fizz_buzz(79) == 3
 ```

This function, `fizz_buzz`, calculates the number of times the digit 7 appears in integers less than the given number which are divisible by 11 or 13. It does so by iterating through the integer up to the given number and checking if the current digit is 7, if it is, incrementing the count. If the count reaches 1 and the current number is divisible by 11 or 13, the count is reset to 0.