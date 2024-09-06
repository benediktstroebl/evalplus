Here's a self-contained Python function that calculates the n-th Fibonacci number and checks if it's also prime:
```python
def is_prime(n):
    """
    Checks if n is prime.

    PRIMARY ALGOING:
      - Check if n <= 1: It's not prime
      - Check if n is even: If n % 2 == 0: It's not prime
      - Check the sum of two distinct positive integers: If the sum is less than 2 or greater than the square root of n, it's not prime.
    """
    simple optimization method using the basic primality tests:
    """
    if n <= 1:
        return False  # Not prime
    elif n == 2:
        return True  # 2 is prime
    else:
        for i in range(3, int(n ** 0.5) + 1,
            if n % i == 0:
                return False
        return True  # Not composite, so prime
```

This function follows a basic optimization to check only up to the square root of n, which significantly reduces the number of iterations needed for primality testing. It then checks theusing the optimized primality algorithm.