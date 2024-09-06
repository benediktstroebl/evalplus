```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` takes a list of integers `lst` as input and returns the sum of the digits of the largest prime number in the list.

The function first filters out all prime numbers from the list using a generator expression, then identifies the largest prime number among them, and finally converts it to a string and sums up its digits to provide the final result.