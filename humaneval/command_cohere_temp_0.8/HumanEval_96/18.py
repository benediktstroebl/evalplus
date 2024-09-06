```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function and if it's prime and less than `n`, it's added to the `primes` list. The loop stops when `count` reaches `n` or exceeds it. This ensures the correct number of prime numbers are collected and returned in the given range. 

The `is_prime()` function is a simple primality test that checks if the number is less than or equal to 1, it immediately returns `False`. It then iterates through numbers from 2 to the square root of the number and checks if the number is divisible by any of them. If there's a divisor, it returns `False`. If it completes the loop without finding a divisor, it returns `True`, indicating the number is prime. 

Overall, the code efficiently solves the problem and meets the requirements of the given challenge.