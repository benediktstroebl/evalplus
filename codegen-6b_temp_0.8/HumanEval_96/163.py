
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
    def is_prime(num):
        """returns True if the num passed in is prime and False otherwise"""
        """
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        else:
            for x in range(3, int(num**(1/2))+1, 2):
                if num % x == 0:
                    return False
        return True
    prime_numbers = []
    i = 1
    while len(prime_numbers) < n:
        if is_prime(i):
            prime_numbers.append(i)
        i = i + 1
    return prime_numbers
