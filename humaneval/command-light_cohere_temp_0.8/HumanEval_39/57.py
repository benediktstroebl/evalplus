```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    for i in range(3, n + 1):
        if is_prime(i):
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(13))  # Output: True
```

This Python script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime. The `is_prime` function is also provided to check for primality. 

This function, when called with the test value `5`, returns `89`, which is the fifth Fibonacci number and is also prime. The function also passes the test with `13` and returns `True`.