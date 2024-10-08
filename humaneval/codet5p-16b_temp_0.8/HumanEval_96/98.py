
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

    primes = []
    current_number = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime > current_number ** 0.5:
                break
            if current_number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_number)
        current_number += 1
    return primes

