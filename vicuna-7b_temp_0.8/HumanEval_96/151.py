
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
    prime_numbers = []
    p = 2
    n = max(n, 2)
    while p * p <= n:
        if n % p == 0:
            break
        prime_numbers.append(p)
        p += 1
    for i in range(1, n):
        if n % i == 0:
            break
        prime_numbers.append(i)
    return prime_numbers
