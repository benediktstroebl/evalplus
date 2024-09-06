```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only the prime numbers using the condition `x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))`. The sum of digits is then calculated for each prime number, which is converted to a string and converted back to an integer using `map(int, str(x))`. The maximum sum of digits is returned among the prime numbers in the list.

This approach effectively solves the problem by finding the largest prime number in the list and calculating the sum of its digits.