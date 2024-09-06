Here is a Python script that provides a self-contained function to solve the problem of counting the number of times the digit 7 appears in numbers less than a given number and divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = 0
        while(i % 11 == 0 or i % 13 == 0):
            num += 1
            i //= 1
        if num == 7:
            count += 1
    return count
``` 
This function will print the number of times the digit 7 appears in numbers less than n and divisible by 11 or 13.