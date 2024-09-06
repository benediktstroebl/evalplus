
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
    def is_prime(n):
        if n > 1:
            if n == 2:
                return True
            elif n % 2 == 0:
                return False
            else:
                for x in range(3, int(n ** 0.5) + 1, 2):
                    if n % x == 0:
                        return False
                return True 
        return False
    result = []
    i = 1
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result
