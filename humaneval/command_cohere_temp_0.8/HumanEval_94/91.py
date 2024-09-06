```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = nums[0]
    max_sum = nums[0] * nums[0]
    for n in nums:
        if primes[n]:
            cur_sum = n * n
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_prime = n
        else:
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    primes[n] = False
                    break
    return max_sum
```

Let's break down the solution step by step:
1. `primes = [True for _ in nums]` initializes a list of boolean values, where each value represents whether the corresponding number in `nums` is prime or not. This initializes with assumption truthfulness for all elements.
2. `max_prime = nums[0]` and `max_sum = nums[0] * nums[0]` initialize the variables `max_prime` and `max_sum` with the first element of the list. We assume that the first element is prime and calculate the initial sum of its digits.
3. The loop iterates through each element `n` in `nums`. If `n` is prime (`primes[n]` is `True`), it calculates the sum of digits of `n` (`cur_sum = n * n`) and updates `max_sum` if the current sum is greater than the previous sum.
4. If `n` is not prime, it goes through each digit `d` from 2 to the square root of `n` (inclusive), and if `n` is divisible by `d`, it sets `primes[n]` to `False`, indicating that `n` is not prime. This optimized step helps reduce the search space for primality checks.
5. Finally, the function returns the `max_sum`, which represents the largest sum of digits among the prime numbers in the list.

The solution is efficient because it does a single pass through the list and uses the primality testing step to narrow down the possible candidates for the largest prime number. This optimizes the digit sum calculation further, improving the overall time complexity.