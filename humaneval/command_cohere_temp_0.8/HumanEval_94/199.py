```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x > 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out integers from the input list that are both prime (not divisible by 2 and greater than 1). It then converts the maximum prime integer to a string and sums the digits to obtain the final result.