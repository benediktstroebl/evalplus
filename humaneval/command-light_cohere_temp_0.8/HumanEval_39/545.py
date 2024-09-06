```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # Checking for prime using primality testing algorithm
        if (n%2 == 0 or n%3 == 0):
            raise ValueError("It is not a prime number")
        # Rest of the numbers are not prime so we return the square of n minus 2
        return (n**2) - 2
``` 
This code defines a function `prime_fib` that returns the n-th Fibonacci number and is also prime. It uses the approach to find prime numbers using the primality testing algorithm, which checks for the prime nature of numbers by observing their divisibility by 2 and 3.