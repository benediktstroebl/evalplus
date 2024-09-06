```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    """
    if n <= 1:
        return 2

    # Check if the number is prime by backtracking
    is_prime = False
    counter = 0
    temp = 2
    while not is_prime:
        if counter > n:
            break
        temp += temp
        counter += 1

    if counter == n:
        is_prime = True

    return temp
```