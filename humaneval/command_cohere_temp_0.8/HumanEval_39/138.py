Here's a Python script with a self-contained function `prime_fib` that solves the problem:
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
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3

    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr

    # This part handles the edge case where n == 0
    # The while loop ensures the last generated number is prime
    while True:
        next_num = prev + curr
        if is_prime(next_num):
            return next_num
        elif next_num < 2:
            break
        prev, curr = curr, prev + curr

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This code defines a function `prime_fib` that generates the n-th Fibonacci number that is also prime. The function handling the prime checking is_prime which checks if a number is prime or not. The code also includes test cases to validate the function `prime_fib`. 

You can copy and paste this code into a Python environment or script to use it. Let me know if you have any questions or if you would like to iterate on this solution!