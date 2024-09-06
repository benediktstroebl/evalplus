

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
    # Store 0th and 1st Fibonacci numbers
    a = 0
    b = 1

    # Store 2nd and 3rd Fibonacci numbers
    c = 1
    d = 2

    # Initialize counter for Fibonacci numbers
    counter = 0

    # Iterate through n
    for i in range(n):
        # Check if current number is a Fibonacci number
        if (a <= i <= b):
            # Check if current number is prime
            if (not is_prime(i)):
                # Update counter and continue with next iteration
                counter += 1
                continue

            # Update next Fibonacci number
            c = a
            d = b + c

        # Update Fibonacci number
        a = c
        b = d

    # Return counter value
    return counter
