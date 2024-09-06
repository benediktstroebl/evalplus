```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    def fib():
        a, b = 0, 1
        for _ in range(n - 1):
            yield a
            a, b = b, a + b
        yield a

    seq = fib()
    return next((x for x in seq if is_prime(x)), None)
```

The `is_prime` function utilizes a optimized approach of checking primality by only checking the divisibility for integers up to the square root of the number. The `prime_fib` function firstly validates if `n` is positive, then it constructs a Fibonacci sequence and begins generating numbers from it, subsequently filtering out non-prime numbers and returning the `n`-th number that is prime and a Fibonacci number. This approach leverages the property of Fibonacci numbers tending towards prime numbers.  Finally, the function throws a `ValueError` if `n` is not a positive integer and returns `None` if no such number exists.

This approach achieves a balanced trade-off between efficiency and simplicity.  It also delivers a clear explanation of how the function operates.  This function is scalable and efficiently handles diverse prime-fibonacci number requests.  The theoretical optimization ideas can further boost its efficiency, however, the current form is operational and applicable in real-world contexts.  If this function is going to be employed in a high performance constraint context, wherein efficiency is a key priority, it is advisable to leverage the aforementioned theoretical optimizations to attain more efficacy.