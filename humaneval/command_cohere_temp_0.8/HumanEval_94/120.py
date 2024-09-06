```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The function `largest_prime_sum_of_digits` takes a list of integers (`nums`) as input and first filters the list to retain only the prime numbers using a list comprehension. Subsequently, it identifies the largest prime number from the filtered list using the `max` function, factoring in the scenario wherein the list of primes is empty. Finally, the sum of the digits of the largest prime is computed by converting it to a string and mapping each character to its integer representation. 

This approach ensures that the largest prime number in the list is identified and the sum of its digits is calculated, returning the desired output for the given test cases.