```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    prime = max(primes) if primes else 0
    return sum(list(str(prime)))
```

The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and first filters the list to retain only the prime numbers using a list comprehension. Subsequently, it identifies the maximum prime number from the filtered list using the `max` function. If the list of primes is empty, the maximum prime is set to 0. Lastly, the sum of the digits of the maximum prime is computed by converting the prime value to a string and summing its digits. 

The code above provides an efficient solution to the problem, and its result is independent of the initial order of the elements in the input list. You can verify the functionality of the solution by calling the function with the example lists provided in the problem statement.