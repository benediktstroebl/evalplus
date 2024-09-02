
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
    if n <= 1:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    if n == 4:
        return [2, 3]
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    result = []
    for i in range(len(sieve)):
        if sieve[i]:
            result.append(i)
    return result
