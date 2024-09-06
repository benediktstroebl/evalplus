Here is a Python script with a self-contained function that solves the problem:
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
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # The n-th Fibonacci prime would be the larger of the two numbers
        # in the (n-1)th Fibonacci pair
        prev, curr = 5, 8
        for _ in range(3, n):
            # Save the previous Fibonacci number
            prev = curr
            # Calculate the next Fibonacci number
            curr = prev + curr
            if is_prime(curr):
                return curr

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` returns the n-th Fibonacci number that is also prime. The `prime_fib` function first checks for some easy cases where n is 1 or 2, then begins calculating the n-th Fibonacci number (beginning from the third Fibonacci number 5 and 8) and checks if each number is prime as it goes. It persistently checks only the newer Fibonacci number (curr) because the prime checks are expensive and the older Fibonacci number (prev) is always prime if the newer one is prime, as they are the two largest prime gaps that occur between Fibonacci numbers. The script also includes tests to help ensure the function works correctly. You can use these tests to verify the correctness of your implementation.  This solution assumes that the input `n` is a positive integer. If `n` is not positive, the function will raise a `ValueError`.  You can use these tests to verify the correctness of your implementation.  If you want to improve this function, you can optimize the `is_prime` function using an iterative approach rather than a recursive approach to solve more efficiently.  This will improve the efficiency of the solution.  Let me know if I can provide any additional assistance with this or any other coding problem!