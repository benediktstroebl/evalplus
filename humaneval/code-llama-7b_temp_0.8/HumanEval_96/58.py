
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
    # my solution
    def is_prime(x):
        if x < 2: return False
        if x == 2: return True
        if x % 2 == 0: return False
        odd_n = range(3,int(x**0.5)+1,2)
        return not any(x % i == 0 for i in odd_n)

    if n < 1: return []
    return [x for x in range(n) if is_prime(x)]

    # cleaner solution
    def is_prime(x):
        return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))

    if n < 1: return []
    return [x for x in range(n) if is_prime(x)]
