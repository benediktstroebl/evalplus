
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
        raise Exception("n cannot be a negative number")
    if n == 0:
        return []
    primes = []
    count = 2
    while count <= n:
        isPrime = True
        for x in range(2, int(count**0.5)+1):
            if count%x == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(count)
        count += 1
    return
