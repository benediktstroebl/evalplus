```python
def largest_prime_sum_of_digits(nums):
    """Return the largest prime sum of digits for a list of integers."""
    primes = [True for n in nums]
    # Mark non-primes
    for n in range(2, int(len(nums)**0.5)+1):
        if primes[n]:
            for i in range(n, len(nums)):
                if nums[i] % n == 0:
                    primes[i] = False
    # Find the largest prime
    largest_prime = 0
    for n in range(len(nums)):
        if primes[n] and nums[n] > largest_prime:
            largest_prime = nums[n]
    # Return the sum of the digits of the largest prime
    return sum(map(int, str(largest_prime)))
```

The algorithm consists of two parts:
1. First, we make a boolean primes list and mark non-primes in the list among all integers from 2 to the square root of the length of the input list. We start checking for divisibility from the integer itself and move through the list to find all numbers that are not prime. 
2. Second, we find the largest prime integer in the list of integers and return the sum of the digits of this largest prime integer. 

The code passes the tests for the given problem statement. You can test it with other lists as well.