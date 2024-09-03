Here is a Python script with a self-contained function that solves the problem you have described:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function
for i in range(50, 78, -1):
    print(fizz_buzz(i), end='\n')
```
This script defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13. The function iterates froms through the numbers from 1 to `n` and checks if the first digit is 7 and whether the number is divisible by 11 or 13. The output will be the expected result of the fizz_buzz function.