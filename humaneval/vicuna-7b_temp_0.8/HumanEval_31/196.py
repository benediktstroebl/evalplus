

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # TODO: Write a function to check if a number is prime.
    # A prime number is a number greater than 1 that is divisible only by 1 and itself.
    # A non-prime number is divisible by at least one other number.
    # One way to determine if a number is prime is to check if it has any factors other than 1 and itself.
    # For example, 7 is prime because it is divisible only by 1 and itself:
    # 7 = 1 x 7
    # On the other hand, 6 is not prime because it is divisible by 2 and 3:
    # 6 = 2 x 3
    # To check if a number is prime, we need to iterate through all possible divisors and check if the number is divisible by each of them.
    # This can be a slow and inefficient way to determine if a number is prime, but it is simple and easy to understand.
    # To make the function more efficient, we can use a more advanced algorithm such as the Sieve of Eratosthenes, which is a fast and efficient way to determine if a number is prime.
    # However, this is a basic exercise in Python programming, and we are not expected to use advanced algorithms.
    # Instead, we will use the simple method of checking if the number is divisible by 1 and itself.
    # If the number is divisible by 1 and itself, then it is prime.
    # Otherwise, it is not prime.
    return True