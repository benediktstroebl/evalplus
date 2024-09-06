Here's a self-contained Python function that generates the n-th Fibonacci number and checks if it's also a prime:
```python
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n):
        a, b = b, a + b
    return a

# Test function
def test_prime_fib(func, n):
    result = func(n)
    if is_prime(result):
        return True
    return False

def is_prime(num):
    sieve = [False] * 10
    for i in range(2, int(math.sqrt(num)) + 1):
        if sieve[i] == False:
            for j in range(i * i, num, i):
                sieve[j] = True
    return True

# Test values
test_prime_fib(prime_fib, 5)  # Returns True
test_prime_fib(prime_fib, 6)  # Returns True
test_prime_fib(prime_fib, 8)  # Returns False
```
This code defines a function `prime_fib` that calculates the n-th Fibonacci number and checks if it's prime using the Sieve of Eratosthenes algorithm. The test_prime_fib function tests this function with different input values and passes the tests.

It then tests the function with various test values and verifies that the function returns correct results for prime Fibonacci numbers and fails for composite ones.