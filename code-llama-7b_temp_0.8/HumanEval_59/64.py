

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # finding the largest prime factor of n (n > 1 and is not a prime)
    # We will keep dividing n by the largest possible prime factor,
    # 2 in this case, until n is no longer divisible by 2.

    # We will create a list of all primes less than or equal to n's
    # square root.
    prime_list = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime_list.append(i)

    # We will loop through the prime list, starting from the end,
    # and check if each number is a factor of n. If it is, we will
    # divide n by that number. If we reach a point where the next
    # prime number is bigger than the remainder, we can stop the
    # loop. This is because prime numbers must be greater than the
    # square root of a number.

    for i in range(len(prime_list) - 1, 0, -1):
        if prime_list[i] <= math.sqrt(n):
            if n % prime_list[i] == 0:
                n /= prime_list[i]
    return int(n)

