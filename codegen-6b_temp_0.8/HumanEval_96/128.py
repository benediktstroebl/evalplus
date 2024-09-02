
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
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n, i):
            is_prime[j] = False

    return [i for i, x in enumerate(is_prime) if x]

