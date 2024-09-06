```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It filters the list to include only prime numbers using the condition `x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))`. The function then finds the maximum sum of digits from the prime numbers using a list comprehension and returns the result.