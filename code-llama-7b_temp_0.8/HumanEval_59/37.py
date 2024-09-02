

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # This can be used to reduce the amount of looping done, but it doesn't work for this problem.
    # return max(get_primes(int(n ** 0.5)) or [1])

    # If n is a prime number, return n.
    if is_prime(n):
        return n

    # This is probably not the fastest way to do this, but I'm gonna do it this way for now.
    # The idea is to divide n by 2 each time, until either 1 or a prime number is returned.
    # Since we're not storing all of the prime numbers, we're just going to add 2 to the last prime number returned.
    # This is a good time to use a loop instead of recursion.
    # This works because we don't need to check if we divided by a prime number before.
    # We'll just divide by 2 and add 2 until we get a prime number back.
    # While we're adding 2 to the last prime number returned, we'll just use the last prime number returned.
    # This will work because if we divided n by a prime number, it will be greater than that prime number.
    # If we divided n by a non-prime number, it will be less than the previous prime number.
    # So, if we divide n by a prime number, then divide n by a non-prime number,
    # we're essentially just dividing n by the first prime number that is less than the previous prime number.
    # This will continue until we get a prime number back.
    prime = 2

    while n > 1:
        if is_prime(n):
            break

        n = n // prime
        prime += 2

    return prime

