

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
    fib_1, fib_2 = 1, 1
    prime = []
    # Index starts from 0, so to take 5th prime fibonacci, we have to set the index to 4.
    index = n - 1
    # Run the loop till index is greater than 0
    while index >= 0:
        # Check if the number is prime, if it is, append it to prime list and decrease index by 1
        if is_prime(fib_2):
            prime.append(fib_2)
            index -= 1
        # Set fib_1 to fib_2 and fib_2 to sum of previous two numbers
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    # Return the last element of prime, which is the n-th prime fibonacci number
    return prime[-1]

