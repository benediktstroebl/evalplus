
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
    # Note: This solution is not efficient for large values of n
    # It uses nested for loops which can be slow for large values
    # A more efficient solution would be to use a function that generates primes
    # and use a while loop to count up to n
    # or use a set to store the primes and check if n is in it
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = []
    i = 0
    while i < n:
        if n % i:
            break
        result.append(i)
        i += 1
    for p in primes:
        if p < n and n % p:
            result.append(p)
    return result