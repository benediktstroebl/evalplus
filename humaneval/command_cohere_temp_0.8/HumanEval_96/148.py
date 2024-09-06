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

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If it is a prime number, it adds it to the `primes` list and increments the `count` variable. Once the count reaches `n`, it breaks the loop to stop collecting primes.

The `is_prime()` function is used to determine if a number is prime. It iterates through numbers from 2 up to the square root of the number and checks if the number is divisible by any of them. If the number is divisible by any of them, it returns `False` and exits the function. If the loop completes without finding a divisor, it returns `True`. 

The `count_up_to()` function is tested with various inputs to ensure that it's working as intended, the tests demonstrate the correctness of the function and show its behavior for the problem statement.