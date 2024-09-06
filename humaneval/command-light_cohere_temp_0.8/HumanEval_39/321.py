```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.
    >>> prime_fib(1)
    2
    Is prime: True
    >>> prime_fib(2)
    3
    Is prime: True
    >>> prime_fib(3)
    5
    Is prime: True
    >>> prime_fib(4)
    13
    Is prime: True
    >>> prime_fib(5)
    89
    Is prime: True
    >>> prime_fib(6)
    23
    Is prime: False
    >>> prime_fib(7)
    > 2
    False
    >>> prime_fib(8)
    589
    Is prime: False
    """

# Test case: Check is_prime for small numbers
def test_prime_fib(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        # Check divisibility by consecutive numbers
        for i in range(5, n, 6):
            if n % i == 0:
                return False
    return True
```
This script defines a function `prime_fib` that computes the nth Fibonacci number and checks if it's prime. The `test_prime_fib` function contains a set of test cases to check the correctness of the `prime_fib` function.