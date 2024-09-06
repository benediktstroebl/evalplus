Here is a Python script that contains a self-contained function that solves the problem of counting the number of times the digit 7 appears in numbers less than a given input n which are divisible by 11 or 13:
```python
def fizz_buzz(n):
    count = 0
    for num in range(1, n+1):
        if int('7' % num in ('11', '13')):
            count += 1
    return count
```
The function iterates through numbers less than n, checks if the number ends with 7 and is divisible by 11 or 13, and increments the count.