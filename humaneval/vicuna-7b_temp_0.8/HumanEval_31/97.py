

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
    # A number is prime if its only divisors are 1 and itself.
    # To test this, we can check if its factors are less than its square root.
    # This is a simple but effective method for testing primality.
    # Note that we need to check up to the square root, because if a number
    # is divisible by any integer from 2 to its square root, then it must
    # also be divisible by all integers from 3 to its square root.
    # So, we can simply check for divisibility by 2 and 3, since those
    # are the only numbers that can be factors of a composite number.
    # We can then use the fact that if a number is divisible by 3,
    # then it must be divisible by its square root (which is also 3).
    # Therefore, if a number is not divisible by 2 or 3, then it must
    # be prime.
    # This method is known as the "trial division" method, because we
    # simply try dividing the number by 2 and 3 and see if it is divisible
    # by those numbers. If it is not divisible, then it is prime.
    # This is a very simple and efficient method for testing primality,
    # and it works for all composite numbers.
    # In fact, this method is so simple and effective that it is one
    # of the most commonly used methods for testing primality.
    # Note that we can also use the Miller-Rabin primality test,
    # which is a much more powerful and efficient method for testing
    # primality, but it is also much more complex and computationally
    # expensive.
    # In this implementation, we use a simple trial division method
    # to check for primality.
    if n < 2:
        # A number is prime if it is greater than 1.
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        # We try dividing the number by 2 and 3, because those
        # are the only numbers that can be factors of a composite number.
        if n % i == 0:
            # If the number is divisible
