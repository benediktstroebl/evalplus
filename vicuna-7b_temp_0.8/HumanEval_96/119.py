
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
    # initialize an empty list
    primes = []
    # check if the input is positive
    if n >= 0:
        # for the first n
        for i in range(n + 1):
            # check if n is divisible by any of the first i numbers
            for j in range(i):
                if n % j == 0:
                    break
            else:
                # if n is not divisible by any of the first i numbers, it is prime
                primes.append(i)
    return primes