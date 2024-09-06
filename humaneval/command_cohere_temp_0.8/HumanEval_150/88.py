Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests:
```python
def is_prime(n):
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

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` that the function should return depending on whether `n` is prime or not. The function uses the `is_prime` function to determine whether `n` is prime and returns `x` or `y` accordingly. The script also includes test cases to verify the function's behavior. 

Note that the `is_prime` function is a simple primality test that only checks divisibility by small numbers and returns true for numbers less than or equal to 3, therefore it is not very efficient and may not work correctly for larger numbers. There are more efficient algorithms for testing primality, such as the Sieve of Eratosthenes.  If you need to test large numbers, consider using those algorithms or other more efficient primality tests. Feel free to include more sophisticated primality tests based on Eratosthenes’s sieve, Miller-Rabin, or AKS primality tests, depending on your requirements and computational efficiency.  If you intend to work with large numbers, consider evaluating the trade-offs of different primality tests.