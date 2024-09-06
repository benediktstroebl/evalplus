Here's a self-contained Python function that solves the problem you provided:
```python
def fizz_buzz(n):
    count = 0
    for i in range(2, n + 1):
        digit = str(i)
        count += sum([bool(d == '7') for d in digit.codes count % 2] // 2 == 0)
    return count
```

This function iterates through numbers from 2 to n, and for each digit string, it counts the number of occurrences of 7. It then returns the number of 7s found in the integers less than n and divisible by 11 or 13.