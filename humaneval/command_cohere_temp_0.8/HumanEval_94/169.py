```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = nums[0]
    max_sum = nums[0]
    for n in nums:
        if primes[n]:
            sum_of_digits = sum(map(int, str(n)))
            if sum_of_digits > max_sum:
                max_sum = sum_of_digits
                max_prime = n
    return max_sum + (max_prime if max_prime != nums[0] else 0)
```

The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and returns the sum of the digits of the largest prime number in the list.

The algorithm operates as follows:
1. Initially, the prime status of each number in the list is assumed to be true, and the first element is taken into consideration as the potential largest prime.
2. The sum of the digits of the potential largest prime is computed and updated if it surpasses the current maximum sum.
3. The element is deemed the largest prime if its digit sum differs from the initial element; otherwise, it is merely a multiple of the initial number, in which case we add the initial number to the result.

This approach efficiently determines the largest prime and computes the sum of its digits within a single pass through the list.