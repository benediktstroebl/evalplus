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

The script defines two functions: `is_prime` checks if a given number is prime, while `count_up_to` returns the first `n` prime numbers less than `n`. 

The `count_up_to` function iterates through numbers from 2 up to `n`, adding each prime number to the `primes` list and incrementing the `count` variable. Once `count` reaches `n`, it breaks out of the loop, returning the list of prime numbers. 

This approach ensures that the function follows the guidelines specified in the problem statement.