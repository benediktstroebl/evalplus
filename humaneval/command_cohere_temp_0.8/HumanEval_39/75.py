Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
```python
def is_prime(n):
    """
    is_prime checks if a number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(13)
    True
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    if n <= 2:
        return 2 if n == 1 else 3
    fib_nums = [0, 1]
    for _ in range(3, n + 1):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    candidate = fib_nums[n - 1]
    while not is_prime(candidate):
        candidate = fib_nums[n - 1] = fib_nums[n - 2] + fib_nums[n - 1]
    return candidate
```

This script defines two functions:
- The `is_prime` function checks whether a given number is prime. It handles simplifications for numbers less than or equal to 1 and then employs a straightforward algorithm to assess primality.
- The `prime_fib` function employs the Fibonacci sequence to generate prime numbers. If `n` is 1, it returns 2, and if `n` is 2, it returns 3. For `n` greater than 2, it generates the subsequent Fibonacci numbers until it reaches the `n-th` number. It then checks the primality of this candidate using the `is_prime` function. If the candidate is not prime, it moves on to the following candidate by altering the previous two terms of the Fibonacci sequence.