
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
    if n == 0:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2,3]
    if not isinstance(n, int):
        raise TypeError('argument to count_up_to must be int, not %s' % type(n).__name__)
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2,3]
    if not isprime(n):
        return [2,3]
    return count_up_to(n-1) + [n]
