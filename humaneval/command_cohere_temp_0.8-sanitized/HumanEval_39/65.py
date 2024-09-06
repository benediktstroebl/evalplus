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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    # Initialize two variables for the Fibonacci sequence where the first element is 0 and the second element is 1
    fib = [0, 1]
    for _ in range(n - 1):
        # Each next number is the sum of the previous two numbers in the Fibonacci sequence
        fib.append(fib[-1] + fib[-2])
    # Check the generated numbers are prime one by one
    for number in fib:
        if is_prime(number):
            return number