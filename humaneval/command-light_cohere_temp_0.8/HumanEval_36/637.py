```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Count the occurrences of 7 in the range 1 to n
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit:
            count += 1
        if (i % 11 == 0 or i % 13 == 0) and count == 0:
            return count
 return count
```