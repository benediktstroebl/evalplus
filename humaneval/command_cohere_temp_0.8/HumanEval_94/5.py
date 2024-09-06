```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` takes a list of integers `lst` as input and returns the sum of the digits of the largest prime number in the list.

The function first selects all prime numbers from the list using a list comprehension. If the list of primes is empty, meaning there are no prime numbers in the list, the function returns 0. Otherwise, it finds the largest prime number in the list using the `max` function and converts it to a string. The function then sums the digits of this string using the `sum` and `map` functions to calculate the sum of the digits of the largest prime number in the list, returning this value.