
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
    count = 0
    ref = [1] * n
    for i in range(2, n):
        if ref[i - 1] == 1:
            count += 1
            for j in range(i, n, i):
                ref[j - 1] = 0
    return range(2, n)[:count]

