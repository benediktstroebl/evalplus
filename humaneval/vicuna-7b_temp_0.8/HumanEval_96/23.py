
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
    # use a list to keep track of prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = []
    # keep track of the current number and the next prime number
    curr = 1
    next_prime = primes[0]
    while curr <= n:
        # if the current number is prime, add it to the result
        if curr % next_prime == 0:
            continue
        result.append(curr)
        # update the current number and the next prime number
        curr += 1
        next_prime += 2
    return result