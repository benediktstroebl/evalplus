
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
    if n <= 0:
        return []

    def is_prime(n):
        """returns if the number is prime"""
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n**0.5 + 1), 2):
            if n % i == 0:
                return False
        return True

    # since we know from the definition we are going to use 1 as the first element in the array
    # so the last element is (n - 1)
    return [i + 1 for i in range(int(n))] if is_prime(n) else []

