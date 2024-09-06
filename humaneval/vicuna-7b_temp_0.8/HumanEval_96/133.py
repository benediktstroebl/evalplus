
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
    # use a function to check if a number is prime
    def is_prime(x):
        if x == 2:
            return True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    # initialize a list with all integers from 2 to n
    primes = range(2, n+1)

    # sort the list in ascending order
    primes.sort()

    # initialize an empty list to store the prime numbers
    result = []

    # iterate through the sorted list
    for i in primes:
        if is_prime(i):
            result.append(i)

    # return the list of prime numbers
    return result
