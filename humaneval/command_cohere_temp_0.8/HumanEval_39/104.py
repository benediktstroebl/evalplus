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
    Returns the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_num = fib_nums[n - 2] + fib_nums[n - 1]
        return fib_num if is_prime(fib_num) else prime_fib(n - 1)

# Dictionary to store Fibonacci numbers
fib_nums = {}

# Initialize the dictionary with the first two Fibonacci numbers
fib_nums[0] = 0
fib_nums[1] = 1

def generate_fib(n):
    """
    Generates Fibonacci numbers and stores them in the fib_nums dictionary.
    """
    if n < 2:
        return
    fib_nums[n] = fib_nums[n - 1] + fib_nums[n - 2]
    if n > 1:
        generate_fib(n - 1)

# Generate the first 10 Fibonacci numbers
generate_fib(10)

print(prime_fib(5))  # It should print 89
```

This script defines a function `prime_fib` that generates Fibonacci numbers and checks if each number is prime using the `is_prime` function. The `fib_nums` dictionary stores generated Fibonacci numbers. The `generate_fib` function is used to generate Fibonacci numbers and populate the `fib_nums` dictionary. The code then calls `prime_fib(5)` and prints the result, which should be `89`. 

Note that the code uses an iterative approach to generate Fibonacci numbers up to the 10th position, which is reasonable for this problem. However, for very large n, the recursive approach might run into limitations due to stack space. But for most practical values of n, the provided solution should work efficiently.