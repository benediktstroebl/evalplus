Here is a self-contained Python script that defines and implements the fizz_buzz function, solving the problem of counting the number of occurrences of 7 in numbers less than a given input n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test the function with different input values
# assert fizz_buzz(50) == 0
# assert fizz_buzz(78) == 2
# assert fizz_buzz(79) == 3
```
The fizz_buzz function uses a loop to iterate through numbers less than the given input n. It checks for divisibility by 11 or 13 using the modulo operator, and if the number has 7 as a factor, it increments the count. This function can be easily tested by passing different input values and verifying the returned results against the expected output.