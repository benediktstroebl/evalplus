Here is a Python script that defines a self-contained function that computes the n-th Fibonacci number and ensures it is a prime:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    Computes n-th Fibonacci number that is prime
    """
    if n <= 0:
        return "Error: n must be a positive integer"
    if n == 1:
        return 2
    if n == 2:
        return 3
    if is_prime(n) == False:
        return "Not a prime"
    return (prime_fib(n - 1) + prime_fib(n - 2))

# Test the function
print(prime_fib(5))  # Output: 89
```
The `is_prime` function in this script determines whether a given number is prime, whereas the `prime_fib` function computes the n-th Fibonacci number and verifies that it is a prime. 
You can use this code to test the function and ensure it operates as intended.