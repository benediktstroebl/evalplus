```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(int(str(max_prime)))</python>
```

The function `largest_prime_sum_of_digits` takes a list of integers (`nums`) as input and aims to find the largest prime number within that list. If the list contains no prime numbers, it returns 0. The function first creates a list of prime numbers from the input list using a list comprehension. Then, it finds the largest prime number within the `primes` list using the `max` function and stores it in the variable `max_prime`. If the `primes` list is empty, indicating no prime numbers in the input, it sets `max_prime` to 0. Finally, the function converts the `max_prime` integer to a string and sums up its digits using the `sum` function, which represents the desired output. 

The code assumes that the list contains at least one integer greater than 1. If the input list is empty or contains only non-positive integers, the function will not function as expected.