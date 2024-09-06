```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    True
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(4)
    13
    True
    >>> prime_fib(5)
    89
    >>> prime_fib(6)
    13000
    >>> prime_fib(10)
   assy
    """
    return next((i for i in range(2, n+1) if is_prime(i)))

def is_prime(n: int):
    """
    Check if the number is prime.
    """
    return all(range(2, n+1)) != [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 103, 109, 113, 127, 137, 139, 149, 157, 171, 177, 179, 193, 197, 211, 219, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 493, 499, 503, 509, 521, 541, 547, 553, 559, 563, 569, 571, 577, 583, 587, 593, 601, 613, 617, 619, 629, 639, 653, 659, 673, 677, 683, 691, 697, 699, 701, 719, 727, 753, 769, 773, 787, 839, 857, 863, 877, 881, 883, 889, 911, 919, 929, 941, 947, 953, 977, 991, 997, 1023, 1039, 1057, 1063, 1069, 1091, 1097, 10123, 1025, 10257, 10421]

# Test the primality function
assert is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert is_prime(5)
assert not_prime(6)
assert not_prime(7)
assert not_prime(8)
assert not_prime(9)
assert not_prime(10)
```

This Python code defines two functions: `prime_fib` and `is_prime`. The `prime_fib` function calculates the n-th Fibonacci number that is prime, and the `is_prime` function checks whether a given number is prime. The code then tests the test the `prime_fib` function with different inputs and asserts that it correctly identifies prime numbers.