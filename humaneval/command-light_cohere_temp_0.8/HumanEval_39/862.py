```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    """
    1 if n <= 1: return 1
    2 if n == 2: return 2
    for i in range(3, n + 1):
        if is_prime(i):
            return i
    return None

def is_prime(n: int):
    """
    checks if the number is prime.
    """
    1 if n <= 1: return False
    2 if n == 2 or n == 3: return True
    for i in range(5, int(n**0.5) + 1,:
        if n % i == 0:
            return False
    return True

# Example usage
print(prime_fib(5))
print(is_prime(6))
``` 
This code defines a `prime_fib` function that returns the n-th Fibonacci number that is prime, and a `is_prime` function that checks if a given number is prime. 

The example usage demonstrates the function with different inputs.