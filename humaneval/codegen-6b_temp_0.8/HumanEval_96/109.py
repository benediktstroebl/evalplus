
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
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    # TODO: Remove this first line which creates a list of size (n + 1)
    primes = [2]
    for i in range(2, n + 1):
        if not is_prime[i]:
            continue  # number is not prime, skip
        for prime in primes:
            if i % prime == 0:
                is_prime[i] = False
                break  # number is not prime, skip
        if is_prime[i]:
            primes.append(i)

    return primes

