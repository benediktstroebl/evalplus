```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    >>> prime_fib(6)
    tastes false
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2  # 2, 3 are the first two prime Fibonacci numbers

    # check if it's a Fibonacci number
    flag, x = 1, n - 1
    while x % 2 == 0:
        x //= 2
    if x == 1:
        flag = 1
        break
    elif flag:
        x = x - 2
    else:
        x = x - 3

    if x < 2:
        return x

    # check for prime
    i = 4
    while i * i <= n:
        if n % i == 0:
            return False
    return True
```  This function efficiently calculates the nth Fibonacci number and verifies if it's prime. It utilizes a strategies like avoiding prime numbers under 4 and dividing by 2 only when the remainder of division by 2 is 1, and checking divisibility by numbers up to the square root of the number.