
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
    # build a list of prime numbers
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    # loop through the range of numbers that we need to count up to
    for i in range(n + 1):
        # check if the current number is prime
        if is_prime(i):
            # add the current number to the list of prime numbers
            prime.append(i)
        # if the number is prime, we have found our answer, stop looping
        if is_prime(i):
            return prime[:n]
    # if we get here, the number is not prime, so we return an empty list
    return []
