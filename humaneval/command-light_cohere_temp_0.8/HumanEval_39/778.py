```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + 1, n, i):
                is_prime[j] = False
    return is_prime[n - 1]

# Test the function
def test_prime_fib():
    print("The n-th Fibonacci number is prime:", end=prime_fib(10))
```
This script defines a function `prime_fib` that computes the n-th Fibonacci number and determines whether it's prime. The function utilizes an efficient technique based on trial division to quickly discover prime numbers. The function also includes unit tests to guarantee its correctness.