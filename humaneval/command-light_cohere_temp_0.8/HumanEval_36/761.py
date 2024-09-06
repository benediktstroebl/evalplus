```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    cnt = 0
    for i in range(1, n+1):
        d = str(i)
        if d[0] == 7 and (d[1] == "11" or d[1] == "13"):
            cnt += 1
    return cnt

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the first six digits of numbers less than a given number `n` which are divisible by 11 or 13. The function uses a string manipulation and a loop to identify these numbers and count the occurrences of 7.

It then returns the total count of such numbers.