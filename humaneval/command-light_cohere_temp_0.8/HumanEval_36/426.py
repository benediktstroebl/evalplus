Here is a Python script that includes the `fizz_buzz` function with self-contained code to solve the problem and pass the tests:

```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    seen = 0
    for num in range(1, n+1):
        digit = ord('7')
        if num % 11 == 0 or num % 13 == 0:
            num = num // 11
        if num < 7 or num > 9:
            seen += (num == digit)
        else:
            seen += 1
    return seen
```