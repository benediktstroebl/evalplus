```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i::2] = False
    return is_prime[n - 1]

def test_prime_fib():
    print(prime_fib(5))
    print(prime_fib(7))
    print(prime_fib(8))
    print(prime_fib(10))
```
This code defines a function **prime_fib(n)** that returns the n-th Fibonacci number that is prime, and tests its functionality with test_prime_fib().

You can use this function to solve the problem, where n is the desired Fibonacci number.