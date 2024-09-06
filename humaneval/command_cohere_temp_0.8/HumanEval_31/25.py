Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and satisfies the given tests because it:
1. Handles Edge Cases: It correctly identifies numbers less than 2 (1, 0, -1, etc.) as not prime.
2. Iterates up to Square Root: It efficiently checks only up to the square root of the number, eliminating the need for unnecessary iterations.
3. Retains Test Cases: It conforms to the provided test cases, including the edge cases and other primes and non-primes highlighted in the original problem.

This optimized approach significantly reduces the number of iterations required for prime checking, making it more efficient for larger numbers.