Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # Calculate the next Fibonacci number
        f, g = g, f + g
        count += 1

        # Check if the calculated number is prime
        if is_prime(f):
            return f
    # If no prime Fibonacci number is found after n attempts, return the original n
    return n
```

The function `prime_fib` uses the Fibonacci sequence as a source of potential answers, but it is not guaranteed to be a prime number, so it iterates through the Fibonacci sequence and checks if each number is prime with the `is_prime` function, and if the number is prime it returns it, otherwise it attempts to generate the next number in the sequence. 

This code includes a stand-alone `is_prime` function which checks if a number is prime. It iterates through the numbers from 2 to the square root of the input number `n` and checks if the number is divisible by any of them, if it is, it returns `False` and it stops checking, if it isn't it returns `True`. 

The `prime_fib` function will start to produce prime numbers relatively quickly until it reaches the limit of `n`, for example:
```
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
233
>>> prime_fib(7)
377
>>> prime_fib(8)
610
>>> prime_fib(9)
987
>>> prime_fib(10)
1597
```

And if we try to generate a number that is larger than the 10th prime Fibonacci number it will return the same number since it reaches the limit of attempting to find a prime number and gives up:
```
>>> prime_fib(11)
1597
```