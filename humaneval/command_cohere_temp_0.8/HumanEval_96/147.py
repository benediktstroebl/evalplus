Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`.  If it is a prime number, it adds it to the `primes` list and increments the `count` counter. Once the counter equals `n`, it stops iterating and returns the `primes` list.

You can verify the functionality of the solution by checking its result for various input values against the example solutions provided in the problem statement.  The `is_prime()` function is also included to ensure the primes are correctly identified.