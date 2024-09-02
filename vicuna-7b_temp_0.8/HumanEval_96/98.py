
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
        for i in range(2,n+1):
            if n % i == 0:
                return False
        return True
    
    def count_up_to_n(n):
        p = [2]
        while p[-1] < n:
            p.append(p[-1]*2)
        prime_numbers = []
        for i in p:
            if is_prime(i):
                prime_numbers.append(i)
        return prime_numbers
    
    return count_up_to_n(n)
