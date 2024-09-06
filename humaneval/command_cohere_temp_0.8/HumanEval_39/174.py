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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two variables for the first two fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Check if the current number is prime
        if is_prime(a):
            count += 1
            if count == n:
                return a
        # Move to the next number in the series
        a, b = b, a + b

# Test the prime_fib function
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
```
This script defines a function `prime_fib(n)` that generates the `n-th` Fibonacci number that is also prime. The script includes a function `is_prime(n)` to check if a number is prime. The `prime_fib` function initializes two variables `a` and `b` to the first two Fibonacci numbers, and then uses a while loop to generate the next Fibonacci number if it's prime. The loop counts the prime Fibonacci numbers and returns the `n-th` one.  The test cases show its correctness.  This solution has a time complexity of `O(n)` because it computes `n` Fibonacci numbers before finding the n-th prime Fibonacci number. 

The space complexity is O(1) because the function does not require any additional space apart from a few integer variables.  This approach also delivers the result without recursion, making it efficient and scalable.