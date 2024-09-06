```python
def largest_prime_sum_of_digits(nums):
    primes = [i for i in nums if is_prime(i)]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits()` takes a list of integers as input and uses the `is_prime()` function to generate a list of prime numbers from the input list. Then it returns the sum of the digits of the largest prime number in this list.

This solution passes the test cases provided in the problem statement.