Here's the Python script with a self-contained function FizzBuzz that calculates the number of times the digit 7 appears in numbers which are either divisible by 11 or 13, and tests it with the provided input range:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    m = 0
    for i in range(1, n+1):
        digit = int('7' + str(i % 10))
        if (i % 11 == 0 or i % 13 == 0) and digit <= n:
            m += 1
    return m

# Test the function
for i in range(50, 78):
    print(fizz_buzz(i), end='')
```
The `fizz_buzz` function calculates the number of times the digit 7 appears in numbers which are either divisible by 11 or 13. It iterates through numbers from 1 to n and extracts the last digit using `str(i % 10)`. Then, it checks if the number is divisible by 11 or 13 and less than or equal to n. If it is, it increments the `m` counter.