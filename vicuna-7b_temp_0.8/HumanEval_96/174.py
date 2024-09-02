
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
    # The first integer we check is 2, since it is the smallest prime number.
    # we check all the numbers that are divisible with 2
    for i in range(2, n+1):
        if not i % 2:
            yield i
            break

    # Then we check the next prime number, which is 3
    for i in range(3, n+1):
        if not i % 3:
            yield i
            break

    # and so on, we keep going until we reach the number n
    for i in range(n+1, len(primes)):
        if not i % any(p for p in primes if p <= n):
            yield i
