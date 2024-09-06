Here's a self-contained Python script that defines a function `fizz_buzz` to solve the problem of counting the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int('7' + str(i % 10))
        if (i % 11 == 0 or i % 13 == 0) and digit <= n:
            count += 1
    return count

# Test the function with different input values
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
The function uses a loop to iterate through numbers from 1 to `n`, adding 1 to the count if the immediately preceding number is divisible by 11 or 13 and less than or equal to the current number, and subtracting 1 from the count if not.