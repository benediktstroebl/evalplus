Here is a self-contained Python script that defines a function `fizz_buzz` solving the problem you provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-laps(7)]
        if digit == "7" and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This function uses a loop to iterate through numbers less than or equal to `n`, and counts how many times the digit 7 appears in the string representation of the number, which is the representation of a number divisible by 11 or 13. It returns the number of times the 7 appears in that range.