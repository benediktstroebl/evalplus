
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
        return n in [2,3,5,7] or n%2 == 0 and n > 2 and n > 3 and n > 5 and n%3 == 0 and n%5 == 0
    
    def count_upto(n):
        result = []
        for i in range(n+1):
            if is_prime(i):
                result.append(i)
        return result
    return count_upto(n)
