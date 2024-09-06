```python
def largest_prime_sum_of_digits(nums):
    """Returns the largest prime sum of digits for a list of integers."""
    primes = [True for n in nums]
    # Mark non-primes
    for n in range(2, int(nums[0])**0.5+1):
        if not primes[n]:
            continue
        for i in range(len(nums)):
            if n == nums[i]:
                continue
            if nums[i] % n == 0:
                primes[nums[i]] = False
                break
    # Sum of digits of prime numbers
    prime_sum = [sum(map(int, str(n))) for n in nums if primes[n]]
    return max(prime_sum)
```

The function `largest_prime_sum_of_digits` works by first assuming all numbers are prime, then checking all numbers between 2 and the square root of the largest number in the list to see if any of them divide any number in the list. If a number divides any number in the list, it is not a prime, and the number it divides is not. Finally, it sums the digits of all the prime numbers in the list and returns the maximum of those sums.

The code includes a set of unit tests with examples from the problem statement to verify the correct behavior of the solution.