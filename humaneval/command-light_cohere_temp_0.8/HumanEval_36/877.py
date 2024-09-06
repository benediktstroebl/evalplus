```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit:
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            break
    return count
``` 
This script defines a function called `fizz_buzz` that solves the problem you provided. The function iterates through the numbers from 1 to n, checks if the current number has the digit 7 (converted to its ASCII integer representation) and if it is divisible by 11 or 13. If the digit is found and the number is divisible by 11 or 13, the function increments the count.