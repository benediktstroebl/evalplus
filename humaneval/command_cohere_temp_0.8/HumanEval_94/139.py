```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It filters out the prime numbers from the list using a generator expression, then finds the maximum sum of digits among those prime numbers by converting each prime to a string and summing its digits. The result is the maximum digit sum of the prime numbers in the list.