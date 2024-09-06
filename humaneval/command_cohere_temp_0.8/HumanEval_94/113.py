```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only prime integers using a primality test for all integers 3 and above, specifically checking whether the number is divisible by any integer between 3 and its square root. Then, it calculates the sum of digits of each prime number in the list and selects the maximum sum, returning the result. 

This solution employs a generator expression to efficiently filter out prime numbers from the list and then computes the sum of digits using Python's built-in `int` and `str` functions.