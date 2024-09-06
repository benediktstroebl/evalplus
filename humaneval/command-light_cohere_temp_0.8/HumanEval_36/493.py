Here is a Python script that contains a self-contained function to solve the problem:

```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    seen = 0
    for num in range(1, n+1):
        d = str(num)[0]
        if d == '7':
            seen += 1
        if (d == '11') or (d == '13'):
            break
    return seen
```

This code defines a function fizz_buzz, which takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop to iterate through the numbers from 1 to n, and keeps track of the first occurrence of the digit 7 using a counter seen. After the first occurrence, we increment the counter and check if there are other occurrences of 7 or 11/13. If there are, we return the count of seen occurrences. If not, we've found all the numbers, and we've seen 7, so the function returns 0.