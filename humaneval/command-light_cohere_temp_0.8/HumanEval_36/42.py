```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    seen_ones = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == 7 and (i % 11 == 0 or i % 13 == 0):
            seen_ones += 1
    return seen_ones
``` 
This function, `fizz_buzz`, calculates the frequency of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function iterates from numbers from 1 to n, and for each number, it extracts the first digit and checks if it is 7 and if the number is divisible by 11 or 13. The frequency of seen 7s is then stored in the `seen_ones` variable.