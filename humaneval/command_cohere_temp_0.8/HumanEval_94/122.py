```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if is_prime(x)]
    return max(sum(map(int, str(p))) for p in primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits(nums)` uses the `is_prime()` helper function to find the largest prime number in the list. Then, for each prime number found, it sums the digits of that number and finds the maximum sum among them. The `is_prime()` function checks whether a number is prime by iterating from 2 up to the square root of the number, if the number is divisible by any of those numbers it is not a prime.