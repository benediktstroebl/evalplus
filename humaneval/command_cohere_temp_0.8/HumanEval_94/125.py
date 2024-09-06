```python
def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out non-prime numbers from the list, and then finds the largest prime number in the list. Finally it converts that number to a string and sums the digits to get the final answer.