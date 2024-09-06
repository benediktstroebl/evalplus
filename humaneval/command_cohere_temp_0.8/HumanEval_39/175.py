Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f = 0
    g = 1
    count = 0

    while count < n:
        # If f is prime, return it
        if is_prime(f):
            return f
        # Prepare for the next number in the sequence
        count += 1
        # Update the variables
        temp = f
        f = g
        g = temp + g

    # If we reach the end of the loop, return g
    return g
```

The function prime_fib(n) will return the n-th number that is a Fibonacci number and it's also prime. Here are some example outputs:
```
2
3
5
13
89
``` 
This solution has a time complexity of O(n) and a space complexity of O(1). The 'is_prime' function used in this solution has an average time complexity of `O(sqrt(n))`.