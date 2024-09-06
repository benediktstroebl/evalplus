```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if is_prime(x)]
    return max(sum(map(int, str(p))) for p in primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits()` takes a list of integers (`nums`) as input and returns the sum of the digits of the largest prime number in the list. The function `is_prime()` checks if a number is prime or not. It returns `True` if the number is prime and `False` otherwise. 

This solution optimally solves the problem without any time complexity issues.