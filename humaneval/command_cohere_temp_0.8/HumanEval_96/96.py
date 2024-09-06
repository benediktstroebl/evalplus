```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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

The script includes a `is_prime` function that checks if a given number is prime or not. The `count_up_to` function initially increments a counter `count`, and a list `primes` to store the prime numbers to be returned. It then iterates from 2 up to `n`, checking each number with the `is_prime` function. If the current number is a prime and less than `n`, it is added to the list, and the counter is incremented. Once the counter reaches `n`, the function breaks out of the loop to avoid unnecessary computations. Finally, it returns the list of primes. 

This solution is efficient and can be optimized further if needed.