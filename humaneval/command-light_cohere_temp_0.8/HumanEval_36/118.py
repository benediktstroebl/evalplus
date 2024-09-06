```python
def fizz_buzz(n):
    return sum(x in [10**i for i in range(1, n+1)] for x in range(0, 9))
```

This function computes the count of digits 7 in numbers less than `n` that are divisible by 11 or 13. The function uses a integer sum to iterate through the numbers from 0 to 9, and checks if each number is divisible by either 11 or 13. 

It returns the number of such such digits found.