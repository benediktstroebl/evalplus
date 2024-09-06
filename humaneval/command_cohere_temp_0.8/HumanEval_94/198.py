```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `nums` to obtain a list of prime numbers, using the condition `x % 2 == 1 and x > 1`. If the list of primes is empty, indicating no prime numbers found, the function returns 0. Otherwise, it proceeds to find the maximum sum of digits by converting each prime number to a string, summing its digits, and selecting the maximum sum amongst them. 

This solution adheres to the problem statement and provides an efficient way to determine the largest prime value while considering the sum of its digits.