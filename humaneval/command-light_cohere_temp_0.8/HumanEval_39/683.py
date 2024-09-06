```python
import math
def prime_fib(n):
    """
    This function returns n-th number that is a Fibonacci number and it's also prime
    :param n: int, required, n-th Fibonacci number
    :return: int, n-th prime Fibonacci number
    """
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    # Check for evenness and divide by 2 if true
    while n % 2 == 0:
        n //= 2
    # The square root of sqrt(n^2) is always prime
    sqrt_n = int(math.sqrt(n **sqrt(n))
    if sqrt_n <= 1:
        # This will handle the case of large numbers, where sqrt(n) is not a integer
        return n
    # The list [2, 3, 5, 8, 13, 21, 34, 55, 89, ...] contains only prime numbers
    return next(filter(lambda x: x > 2 and x != int(x) and x != int(math.sqrt(x) and x % 2 == 0, [2, 3, 5, 8, 13, 21, 34, 55, 89, ...]), n)
```
This code defines a function called `prime_fib` that calculates the nth Fibonacci number and ensures it is prime. It achieves this by following steps:
1. Check if n is less than 0. If so, raise a ValueError.
2. Check if n is 1. If so, return 2. If n is 2, return 3.
3. Check if n is even odd. If so, divide n by 2 and continue.
4. Check if sqrt(n^2) is less than or equal to 1.
5. Check if sqrt(n^2) is greater than 1. If so, return n directly.
6. Use the filter function to find the list of primes greater than 2, excluding the square roots of negative numbers and the int(sqrt(x)) value x where x is a prime but not equal to 2.

The function handles large numbers by using the math.sqrt function to calculate the square root. It ensures that the list contains only prime numbers greater than 2.

Note: This implementation assumes that the input n is a positive integer.  If n is not a positive integer, the function may raise an error.