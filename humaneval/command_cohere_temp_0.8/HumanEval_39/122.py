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

def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Starts with larger prime Fibonacci numbers
        num = 10 ** (n - 2).bit_length()
        return prime_fib(num)[0]

def generate_primes_and_fibs(n):
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    else:
        # Starts with larger prime Fibonacci numbers
        num = 10 ** (n - 2).bit_length()
        return prime_fib(num) + generate_primes_and_fibs(num)

# Tests
assert 2 == prime_fib(1)
assert 3 == prime_fib(2)
assert 5 == prime_fib(3)
assert 13 == prime_fib(4)
assert 89 == prime_fib(5)

assert [2, 3] == generate_primes_and_fibs(2)
assert [2, 3, 5] == generate_primes_and_fibs(3)
assert [2, 3, 5, 13] == generate_primes_and_fibs(4)
assert [2, 3, 5, 13, 89] == generate_primes_and_fibs(5)
```