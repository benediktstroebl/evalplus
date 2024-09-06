
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
        """A helper function that checks if a number is prime or not."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def count_up_to_n(n):
        """
        The main function that counts up to n and returns an array of prime numbers less than n
        """
        if n <= 1:
            return []
        prime_numbers = []
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i):
                prime_numbers.append(i)
                while i < n:
                    if is_prime(i):
                        prime_numbers.append(i)
                    i += 1
        return prime_numbers
    return count_up_to_n(n)
