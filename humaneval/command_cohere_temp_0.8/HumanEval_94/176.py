```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out odd numbers and numbers greater than 1, which leaves only prime numbers. Then, it finds the maximum prime number, converts it to a string, and sums the digits to get the final answer.