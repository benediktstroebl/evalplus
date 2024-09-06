def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    else:
        # First Fibonacci number that is prime
        fib_prime = 2
        # Second Fibonacci number that is prime
        second_fib_prime = 3
        count = 2
        while True:
            if is_prime(fib_prime) and is_prime(second_fib_prime):
                if n == count:
                    return fib_prime
                elif n == count + 1:
                    return second_fib_prime
                count += 2
            elif is_prime(fib_prime):
                fib_prime = fib_prime + second_fib_prime
                second_fib_prime = fib_prime - fib_prime
            else:
                # Start the process again with the next Fibonacci number
                fib_prime = second_fib_prime + 2 * fib_prime
                second_fib_prime = fib_prime - fib_prime