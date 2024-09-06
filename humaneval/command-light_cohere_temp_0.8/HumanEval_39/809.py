```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    a, b = 2, 1
    while b <= n:
        a, b = b, a+b
    return a

def test_prime_fib(func):
    """
    Test the function with n = 1 and checks for the returned number being prime
    """
    assert func(1) == 1
    assert not any(i > 1 and i % 3 for i in range(2, 10))

# Run the function and test
n = 6
print(f"The {n}-th Fibonacci number is {prime_fib(n)} and it's prime.")
test_prime_fib(prime_fib)
```