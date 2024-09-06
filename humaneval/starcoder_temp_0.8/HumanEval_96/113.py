
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
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non negative.")
    if n == 0:
        return []
    primes = [2]
    for i in range(3, n + 1, 2):
        prime = True
        for j in range(3, i, 2):
            if i % j == 0:
                prime = False
        if prime:
            primes.append(i)
    return primes
