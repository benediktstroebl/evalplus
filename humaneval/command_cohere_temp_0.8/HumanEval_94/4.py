```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers as input and returns the largest sum of digits among the prime numbers in the list.

The list comprehension filters out non-prime numbers, then the max sum of digits is calculated using a generator expression within the sum function, converting each prime number to a string and summing its digits. 

This approach ensures efficiency and simplicity while handling the given problem.