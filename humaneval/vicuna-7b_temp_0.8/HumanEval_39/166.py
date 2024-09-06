

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Ensure n is positive
    if n < 2:
        raise ValueError("n must be positive")
    
    # Check for special cases
    if n == 2:
        return 1
    elif n == 3:
        return 1
    elif n == 5:
        return 3
    elif n == 89:
        return 89
    
    # Start with first two Fibonacci numbers
    a, b = 0, 1
    # Use an array to store prime numbers
    primes = [True]
    
    # Iterate over the remaining numbers
    for num in range(2, n):
        # Check if the number is prime
        if num > 1:
            if num in primes:
                continue
            # If the number is not already in the array, add it
            primes.append(num)
        # If the number is not prime, skip it
        else:
            for p in primes:
                if num % p == 0:
                    break
            else:
                continue
    
    # Return the n-th Fibonacci number
    return a
