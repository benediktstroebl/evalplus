
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
    if n < 0:
        return []
    if n < 2:
        return []

    # a prime number is only divisible by 1 and itself
    primes = [2,3]
    for n in range(5, n + 1):
        for divisor in primes:
            if divisor > n ** 0.5:
                primes.append(n)
                break
            elif n % divisor == 0:
                break
        else:
            primes.append(n)

    return primes
