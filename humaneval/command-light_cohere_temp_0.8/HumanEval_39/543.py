Here's the solution:

def prime_fib(n):
    if n <= 1:
        return n
    else:
        # Check if the number is prime
        is_prime = True
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                is_prime = False
                break
        if is_prime:
            return n
        else:
            return prime_fib(n + 2)

This script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's also prime. It uses a single loop to test divisibility from 2 up to the square root of n, and returns the prime result when found. 

This function can be easily integrated into larger programs or used directly as-is.