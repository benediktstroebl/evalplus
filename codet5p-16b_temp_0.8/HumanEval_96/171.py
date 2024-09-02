
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

    primes = [2,3,5,7]
    if n >= 7:
        primes.append(11)
    if n >= 17:
        primes.append(13)
    if n >= 19:
        primes.append(17)
    for i in range(19, n+1):
        prime = True
        for divisor in primes:
            if i % divisor == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes
