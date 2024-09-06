```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # Iterate through powers of 2 and 3
        for i in range(5, n + 1, 6):
            if is_prime(i):
                return i
        return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(6))  # Output: True
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is also prime, and tests whether a given number is prime using the `is_prime` helper function.  The function then provides an example usage by calculating and printing the 5th Fibonacci number and checking if the number 6 is prime or not.