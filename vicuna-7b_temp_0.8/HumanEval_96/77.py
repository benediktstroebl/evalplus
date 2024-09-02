
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    # variable to store the next prime number
    next_prime = 2
    # variable to store the count of prime numbers less than n
    count = 0
    # variable to store the prime numbers less than n
    primes = []
    # check if n is 0
    if n == 0:
        return []
    # check if n is 1
    elif n == 1:
        return []
    # check if n is prime
    elif n > 1:
        # if n is prime, add it to the list of primes
        if n != next_prime:
            primes.append(n)
            # increment the next prime number
            next_prime = 2 * (next_prime + (n - 1))
    # add all the prime numbers less than n to the list
    for prime in primes:
        count += 1
        count_up_to(n - prime)
    return count