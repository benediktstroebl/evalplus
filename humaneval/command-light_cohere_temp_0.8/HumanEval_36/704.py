Here is a self-contained Python script that defines a function fizz_buzz that solves the problem you have provided:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum_of_7s = 0
    for i in range(1, n+1):
        num = pow(10, i) + 7
        if (num % 11 == 0) or (num % 13 == 0):
            sum_of_7s += 1
    return sum_of_7s
```

This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the range of integers less than a given input n, which are divisible by either 11 or 13. The function iterates through numbers from 1 to n, and checks if the number is either divisible by 11 or 13. It then counts the process by adding 1 to the sum of 7's, which represents the frequency of the digit 7 in the numbers divisible by 11 or 13.