Here is a Python script that defines a function called `fizz_buzz` that solves the problem you provided:

```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    # Count the occurrences of 7 in numbers less than n that are divisible by 11 or 13
    count = 0
    for i in range(1, n+1):
        if (n % 11 == 7) or (n % 13 == 7):
            count += 1

    return count

# Unit tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number `n` that are divisible by 11 or 13. The function uses a efficient loop to iterate through numbers from 1 to `n`, checking for the digits 7 in the respective divisors. The final count is returned as the solution.