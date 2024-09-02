
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
    # if n is 0, return an empty array
    # if n is 1 or less, return an empty array
    if n <= 0:
        return []

    # if n is 1, return an array with n
    if n == 1:
        return [1]

    # initialize the counter to 1
    counter = 1

    # initialize an empty array to store the prime numbers
    primes = []

    # loop until the counter is less than or equal to n
    while counter <= n:
        # check if the counter is prime
        if is_prime(counter):
            # if the counter is prime, add it to the array of primes
            primes.append(counter)
        # increment the counter
        counter += 1

    # return the array of primes
    return primes


