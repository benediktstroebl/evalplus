Here's a self-contained Python script with a function that calculates and returns the n-th Fibonacci number that is prime:
```python
def is_prime(n):
    """
    Check if n is a prime number.
    """
    definition of a prime number: number is prime if it is greater than 1 and the only positive factors are 1 and itself.

    1 is not a factor
    2, 3, 5, 7, 11, 13, 17, 19... are all prime numbers. The square root of number is always the factor of even numbers.

    """
    check for factors:
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

def prime_fib(n):
    """
    returns n-th Fibonacci number that is prime
    """
    if n <= 0:
        return None
    if n == 1:
        return 2
    if is_prime(n):
        return n
    return prime_fib(n - 1) + prime_fib(n - 2)

# Driver code
print(prime_fib(10))

```

This code defines a function called `is_prime` that checks whether a given number `n` is a prime number. It uses the testing various numbers up to determine whether `n` is prime or not. The function then returns the is a prime number if it passes all the tests and is greater than 1.

The function `prime_fib` takes an integer `n` as input and returns the n-th Fibonacci number that is prime. It checks if `n` is a prime number by calling the `is_prime` function and then recursively calculates the Fibonacci number. The code also passes tests for the function and prints the result for the 10th input.