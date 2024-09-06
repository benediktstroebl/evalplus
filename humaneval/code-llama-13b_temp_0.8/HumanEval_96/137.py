
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

    # init
    primes = []
    # for each n in range 2 to n-1
    for i in range(2, n):
        # for each number in range 2 to n-1
        for j in range(2, i):
            # check if i is divisible by j
            if i % j == 0:
                # if it is, break out of this loop
                break
            # else, it is prime
            if j == i - 1:
                primes.append(i)
                break

    # return primes
    return primes

