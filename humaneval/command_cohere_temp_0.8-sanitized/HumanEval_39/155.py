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
    Generates the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the Fibonacci number to be generated.

    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    
    while not is_prime(fib[n]):
        fib[n] += 1
    
    return fib[n]