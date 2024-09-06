```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It filters the list to include only prime numbers using a list comprehension and checks for divisibility by all odd numbers less than or equal to the square root of the number. The maximum sum of digits is then calculated by converting each prime number to a string and summing its digits. This value is returned as the output of the function.