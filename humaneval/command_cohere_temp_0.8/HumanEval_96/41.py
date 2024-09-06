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
    """Return an array of the first n prime numbers less than n"""
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

This script contains a function called `count_up_to(n)` that returns an array of the first `n` prime numbers that are less than `n`. The script also includes a function called `is_prime(n)` that checks if a number is prime. This is used by `count_up_to(n)` to iterate through numbers from 2 up to `n`, adding each prime number to the `primes` array until it has collected `n` primes. 

Here is an example output to validate the correct operation of the script:
```
count_up_to(5) => [2, 3]
count_up_to(11) => [2, 3, 5, 7]
count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
```