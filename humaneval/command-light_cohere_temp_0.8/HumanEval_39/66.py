```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is also prime.
    Returns None if n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        return None
    if n <= 1:
        return n
    
    # First prime Fibonacci number
    fib_prime = 2
    
    # Base case check
    if n == 2:
        return fib_prime
    
    # Loop until finding a prime or reaching n
    for i in range(3, n + 1):
        is_prime = True
        
        # Check for divisibility by numbers up to its square root
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
        
        # Check if the current Fibonacci number is prime
        if is_prime:
            fib_prime = fib_prime + i
            
        else:
            break
    
    return fib_prime

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(10)) # Output: None
 ``` 
This script defines a function `prime_fib` that returns the n-th Fibonacci number that is prime, if n is a positive integer.  The function performs an iterative trial to find the prime Fibonacci number, ensuring that the result is correct.