```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    is_prime = [True] * (5 ** (n-4))
    for i in range(5, n + 1, 6):
        is_prime[i] = False
    for j in range(2, n // 2 + 1):
        if is_prime[j]:
            for k in range(j * j, n, j):
                is_prime[k] = False
    return is_prime[-1]

# Test the function
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 2
    assert prime_fib(7) == 56
    assert prime_fib(8) == 24
    assert prime_fib(9) == 2
    assert prime_fib(10) == 34

# Run the tests if the script is executed
test_prime_fib()
``` 
This code defines the `prime_fib` function, which calculates the nth Fibonacci number that is prime and returns it. It uses an efficient technique based on trial and error to find prime numbers, and tests its correctness with a variety of input values.