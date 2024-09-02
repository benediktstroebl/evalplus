
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
    count_up = 0
    list_of_primes = []
    for i in range(2,n):
        if (i <= 1) or (i % 2 == 0):
            count_up += 1
            continue
        for j in range(3, i // 2 + 1):
            if i % j == 0:
                break
        else:
            list_of_primes.append(i)
            count_up += 1
    return list_of_primes
