```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to obtain a list of prime numbers, using the condition `x % 2 == 1 and x > 1`. If the list of primes is empty, indicating no prime numbers are found, the function returns 0. Otherwise, it converts the maximum prime to a string and sums the digits to return the answer.