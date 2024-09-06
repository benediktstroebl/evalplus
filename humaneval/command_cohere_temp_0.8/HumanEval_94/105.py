```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    sqrts = [int(n**0.5) for n in nums]
    f = 0
    for i, n in enumerate(nums):
        if primes[i] and sqrts[i] * sqrts[i] == n:
            f = max(f, sum(map(int, str(n))))
    return f
```

The function iterates over the list of integers, for each integer it first determines if it is prime and its square root, then checks if the integer is a perfect square and updates the maximum sum of digits `f` accordingly. The function eventually returns the maximum sum of digits of any perfect square in the list.