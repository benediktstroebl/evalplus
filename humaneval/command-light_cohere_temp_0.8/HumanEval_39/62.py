```python
import math

def prime_fib(n):
    """
    returns n-th number that is a Fibonacci number and is prime
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
    >>> prime_fib(6)
    648
    >>> prime_fib(10)
    534567

    It uses a simple heuristic: It checks if the sum of two consecutive digits is less than 6, then it knows the number is prime.
    """
fibonacci = [0, 1]
for _ in range(n):
    a, b = fibonacci[-1], fibonacci[-2]
    fibonacci.append([a[(a + b) // 6] % 9)

def is_prime(n):
    """
    simple test using sum of digits
    >>> is_prime(2)
    True
    >>> is_prime(3)
    False
    >>> is_prime(5)
    True
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(12)
    True
    """
    return n <= 1 or sum(map(int, str(n))) % 1 == 0

def test_prime():
    """
    >>> test_prime(is_prime(2))
    True
    >>> test_prime(is_prime(3))
    False
    >>> test_prime(is_prime(5))
    True
    >>> test_prime(is_prime(7))
    True
    >>> test_prime(is_prime(10))
    False
    >>> test_prime(is_prime(12))
    True
    """
    return map(is_prime, range(2, 100))

#Call the functions
prime_fib = [lambda n: fibonacci[n % len(fibonacci)]]
is_prime = [lambda n: sum(map(int, str(n))) % 1 == 0]

print(prime_fib(15))
print(test_prime(15))
```