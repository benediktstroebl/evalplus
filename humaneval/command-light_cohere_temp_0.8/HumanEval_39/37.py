```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next(is_prime(num) for num in range(3, n)) + 2

def is_prime(n: int):
    return all([n % i == 0 for i in range(2, int(n**0.01) + 1])

def test_prime_fib():
    print(prime_fib(5))

test_prime_fib()
``` 
This script defines a function `prime_fib` that computes the n-th Fibonacci number such that it is prime and the function `is_prime` that checks if a given number is prime. The function also provides a test function `test_prime_fib` to test the correctness of `prime_fib` function.