
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
    # Our list of primes
    prime_list = []

    # loop through all the numbers
    for number in range(2, n + 1):
        # loop through all the numbers we have already
        is_prime = True
        for prime in prime_list:
            # if we find a number that divides evenly into our current number
            # it is not prime, so break and start the next iteration
            if number % prime == 0:
                is_prime = False
                break
        # if we didn't find a number that divided evenly into our current number
        # add it to our list of primes
        if is_prime:
            prime_list.append(number)
    return prime_list

