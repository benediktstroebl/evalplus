```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = nums[0]
    max_prime_sum = nums[0]
    for n in nums:
        if primes[n]:
            if n > max_prime:
                max_prime = n
                max_prime_sum = n
            elif n == max_prime:
                max_prime_sum = max(max_prime_sum, n)
        else:
            primes[n] = True
    return max_prime_sum
```

The function `largest_prime_sum_of_digits` takes a list of integers `nums` as input and returns the largest prime value's sum of digits.

The script uses a list comprehension to initialize a boolean list `primes`, indicating whether each element in `nums` is prime or not. The function then iterates through the list, considering each number as a potential prime. If a number is prime and larger than the current `max_prime`, it updates both the `max_prime` with the number and the `max_prime_sum` with the number's value. If a number is not prime, it marks it as such in the `primes` list to avoid processing it again. Finally, it returns the `max_prime_sum`, which will be the sum of digits of the largest prime value in the list.