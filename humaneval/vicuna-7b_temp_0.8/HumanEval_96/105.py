
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
    def is_prime(x):
        if x == 2:
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def count_up_to_n(n):
        #if n == 0 or n == 1 return []
        primes = []
        for i in range(1, int(n ** 0.5) + 1):
            if is_prime(i):
                primes.append(i)
        return primes
    return count_up_to_n(n)
