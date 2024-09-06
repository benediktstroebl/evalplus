
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
    # FIRST: convert the input to a list of the first n integers
    int_list = []
    for x in range(n):
        int_list.append(x)
    # SECOND: create an empty list to store the primes
    prime_list = []
    # THIRD: loop through the list and check the number to see if it is prime
    for x in int_list:
        # first, check if the number is a prime
        if is_prime(x):
            # if it is, add it to the prime list
            prime_list.append(x)
    return prime_list
