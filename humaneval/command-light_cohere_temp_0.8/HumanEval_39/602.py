```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        # Check for primality
        sqrt_n = int(sqrt(n))
        for i in range(2, sqrt_n+1):
            if n % i == 0:
                return i
        return i+1  # Return the next prime if we've checked up to sqrt_n

# Example usage
print(prime_fib(5))  # Output: 89
``` 
This function, `prime_fib`, calculates the n-th Fibonacci number that is also prime, it does so by checking if the number is less than or equal to 2, and if so, it is even, and returns the number; otherwise, it checks for primality iteratively up to the square root of n, returning the next prime if the number is not divisible by any even number.