```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        a, b = 5, 2
        for _ in range(n - 4):
            a, b = (a + b) % 1, b + 1
        return a

# Test function for primality
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

# Test and print function
def test_and_print():
    n = 10
    print("The {}th Fibonacci number is {}".format(n, prime_fib(n)))
    print("Is {} prime?".format(n), end=" ")
    for i in range(2, n+1):
        if is_prime(i):
            print("Yes"*" ", end="")
    print()

# Test and print function
test_and_print()
``` 
This script defines a function `prime_fib` that computes the n-th Fibonacci number and tests for prime numbers up to n. It also includes a test function `is_prime` to check for primality and a `test_and_print` function to test the `prime_fib` and print the results.  This test function is a way to solve this problem in a self-contained manner.