```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2 if is_prime(n) else next(prime_fib(n+1))

def is_prime(n: int):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def prime_fib_test():
    assert prime_fib(5) == 89
    assert is_prime(5)
    assert prime_fib(4) == 13
    assert not is_prime(0)
    assert not is_prime(6)
    assert not is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)

# Test suite
if __name__ == "__main__":
    prime_fib_test()
```
The function `prime_fib` computes the n-th Fibonacci number that is also prime. The function `is_prime` checks whether a given number is prime. The function then uses these `prime_fib` and `is_prime` helper functions to test the correctness of its implementation.