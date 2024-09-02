
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
    if n < 2:
        return []
    prime_no = [False for i in range(n)]
    prime_no[0] = prime_no[1] = False
    for i in range(2, n):
        if not prime_no[i]:
            continue
        for j in range(2 * i, n, i):
            prime_no[j] = False
    return [i for i in range(2, n) if prime_no[i] == True]

