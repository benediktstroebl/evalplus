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

The function `is_prime` is used to check if a number is prime. Then, the function `count_up_to` starts counting from 2 up to *n* and stores each prime number in the primes list until it collects *n* primes or reaches *n*, whichever comes first. 

This solution passes all the test cases mentioned in the original prompt. You can test it via calling the function with different input values. 
If there is anything else I can help with, let me know!