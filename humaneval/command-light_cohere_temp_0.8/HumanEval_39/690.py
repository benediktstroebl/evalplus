```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    Return 0 if n <= 1, else is it a Fibonacci number?
    """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return 2
    prime = True
    temp = prime_fib(n // 2)
    while prime:
        prime = False
        num = temp + (temp * (n % 2))
        if (num <= 1):
            prime = True
        else:
            temp = num
    return temp
```