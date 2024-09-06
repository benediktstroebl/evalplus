
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
        """simple function that checks if n is a prime number"""
        if (n <= 1):
            return False
        if (n == 2):
            return True
        if (n % 2 == 0):
            return False

        max = math.ceil(math.sqrt(n))
        i = 3
        while (i <= max):
            if (n % i == 0):
                return False
            i = i + 2

        return True

    count = 0
    result = []

    while count < n:
        if is_prime(count):
            result.append(count)
            count += 1
        else:
            count += 1

    return result

