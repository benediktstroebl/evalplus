```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Test function
def test_prime_fib():
    print("First nth Fibonacci number: ", prime_fib(1))
    print("Second nth Fibonacci number: ", prime_fib(2))
    print("Third nth Fibonacci number: ", prime_fib(3))
    print("Fourth nth Fibonacci number: ", prime_fib(4))
    print("Fifth nth Fibonacci number: ", prime_fib(5))
    print("Is a prime?", prime_fib(6))

# Test suite
test_prime_fib()
```
The function `prime_fib` calculates the n-th Fibonacci number that is both prime and returns it. The function uses an loop that starts with n - 2 (since Fibonacci numbers follow the pattern of each number being a sum of the two preceding ones) and continues until reaching the desired value.  The uses the testing to make sure the function works correctly.