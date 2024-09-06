
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
    # create list of all prime numbers less than n
    primes = [x for x in range(2,n+1) if x % 2 == 1]
    # filter out prime numbers greater than n
    primes = filter(lambda x: x < n, primes)
    # count the number of prime numbers less than n
    return len(primes)
