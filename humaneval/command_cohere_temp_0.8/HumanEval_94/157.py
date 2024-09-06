```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The provided Python script defines a function `skjkasdkd` that takes a list of integers as input (`lst`). This function first filters the list to retain only the prime numbers using a list comprehension. It identifies the maximum prime number using the `max` function with an optional `if primes else 0` clause to handle the case where no prime numbers are found. Finally, it calculates the sum of the digits of the largest prime number by converting it to a string and mapping each character to its integer value using `map(int, str(max_prime))`. The result is the desired output.