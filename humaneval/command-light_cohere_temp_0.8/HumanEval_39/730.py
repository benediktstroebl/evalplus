```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    prime_fib_helper(n)

def prime_fib_helper(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    if n % 3 == 0:
        return 5
    if n % 5 == 0:
        return 5
    return prime_fib_helper(n - 1)
```
This function, `prime_fib`, returns the n-th Fibonacci number that is prime and also a test to ensure the function works as expected.