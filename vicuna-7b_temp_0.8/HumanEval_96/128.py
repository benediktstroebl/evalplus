
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
        """
        :param n: an integer
        :return: True if n is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        for num in range(2, int(n**0.5) + 1):
            if n % num == 0:
                return False
        return True
        
    primes = []
    for num in range(1, n+1):
        if is_prime(num):
            primes.append(num)
            if num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if is_prime(num * i):
                        primes.extend([num*i] * (int(num**0.5) + 1) // i)
                        break
    return primes
