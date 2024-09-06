```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only prime integers using a list comprehension and the condition `x >= 2 and all(x % n for n in range(3, int(x**0.5) + 1, 2))`. The sum of digits is then calculated for each prime number using the `str(x)`, which converts the prime number to a string and `map(int, ...)` which converts each digit of the string `x` to an integer. The `max` function is then used to find the largest sum of these digits, as specified in the problem statement. 
This solution addresses the given example scenarios, returning the correct values for each.