
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
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
    i = 0
    result = []
    while i < n:
        if n % i:
            result.append(i)
            n = n//i
        else:
            result.append(i)
            i += 1
    return result

