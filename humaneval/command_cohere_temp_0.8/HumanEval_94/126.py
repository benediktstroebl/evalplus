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
1. `primes` List Initialization: The `primes` list is initialized with `True` values for each element in the input list. Each `True` value indicates that the corresponding number is prime.
2. Maximum Prime and Sum Initialization: The initial maximum prime value and its corresponding maximum digit sum are both set to the first element of the input list. Initially, we assume that the first element is the largest prime.
3. Loop Through Input List: The code then iterates through each element `n` in the input list.
4. Prime Check: If `n` is marked as prime in the `primes` list, it means `n` is a prime number. The code then calculates the digit sum of `n` (squared) and updates `max_sum` if the new sum is greater than the previous one. Additionally, the variable `max_prime` is updated to reflect the current maximum prime.
5. Non-Prime Check: If `n` is not marked as prime, the code checks if `n` is divisible by any number from 2 to the square root of `n`. If `n` has any divisors within this range, it's not a prime, and the corresponding `primes[n]` is set to `False`.
6. Final Output: After iterating through all elements in the input list, the function returns the `max_sum`, which represents the largest prime sum of digits.

The approach leverages the fact that prime numbers tend to have fewer digits, and therefore computing the sum of digits is an efficient way to confirm a prime number. Additionally, the divisibility check helps efficiently rule out non-prime numbers.