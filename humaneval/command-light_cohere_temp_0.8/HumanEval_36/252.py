Here's a self-contained Python script with a function that calculates the number of times the digit 7 appears in numbers that are less than n and are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        d = str(num)
        if (d == "77") or ((d[0] == "7") and (d[1] >= "0") and (d[1] <= "4")):
            count += 1
    return count
```

This function iterates through numbers from 1 to n, and counts the number of 7s or strings starting with 7, which are divisible by 11 or 13.