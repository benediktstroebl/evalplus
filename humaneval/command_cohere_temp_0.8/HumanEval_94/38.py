```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if is_prime(x)]
    return max(map(sum_of_digits, primes))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(d) for d in str(n))
```
The function `largest_prime_sum_of_digits(nums)` returns the largest sum of digits among the largest prime integers in the list `nums`. The function `is_prime(n)` checks if a number is prime and `sum_of_digits(n)` calculates the sum of digits of a number. The code uses `map()` to apply the `sum_of_digits()` function to each element in the `primes` list, and `max()` to find the largest sum of digits.