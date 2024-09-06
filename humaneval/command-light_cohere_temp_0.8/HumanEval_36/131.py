Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-()[-1:]
        if digit == "7" and int(digit) <= 4:
            count += 1
    return count

# Test case 1
assert fizz_buzz(50) == 0

# Test case 2
assert fizz_buzz(78) == 2

# Test case 3
assert fizz_buzz(79) == 3
```

This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function iterates through numbers in a loop and checks if the last digit is 7 and if the number is less than or equal to 4. The result is then counting the occurrences of the digit 7.