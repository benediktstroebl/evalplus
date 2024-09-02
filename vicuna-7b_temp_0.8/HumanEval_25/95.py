from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Prime number is a number that is divisible only by 1 and itself
    # Therefore, all non-prime numbers are divisible by at least one prime number
    # and we can divide all numbers by all known prime numbers and see if the remainder is 0
    # this will give us all factors of the number
    # and we can use a queue to keep track of divisor, divisor of divisor and so on

    # Initialize the queue with the number
    divisor = [n]
    while len(divisor) > 0:
        # Get the last divisor from the queue
        last_divisor = divisor[-1]
        # Get the factorial of the last divisor
        last_divisor_fact = last_divisor!
        # Multiply all the elements in the queue by the last divisor_fact
        for i in range(len(divisor)):
            divisor[i] = last_divisor*divisor[i]

        # Add the last divisor to the queue
        divisor.append(last_divisor)

        # Remove the last divisor from the queue
        divisor.pop()

    # Sort the list of divisors in non-descending order
    divisors = sorted(divisor, reverse=True)

    # Create a list of prime factors
    prime_factors = []
    # Iterate through the list of divisors
    for div in divisors:
        # If the number is divisible by 2 only
        if div == 2:
            # We can stop, because 2 is the only factor
            prime_factors.append(1)
        # If the number is divisible by 3 only
        elif div == 3:
            # We can stop, because 3 is the only factor
            prime_factors.append(1)
        # If the number is divisible by 4 only
        elif div == 4:
            # We can stop, because 4 is the only factor
            prime_factors.append(1)
        # If the number is divisible by 5 only
        elif div == 5:
            # We can stop, because 5 is the
