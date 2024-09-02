
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

    def is_prime(number):
        """returns true if number is a prime number, false otherwise."""
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def get_array_from_number(number):
        """returns an array of prime numbers from 2 to number. If number is prime, includes it in the array"""
        if number == 1:
            return []
        if is_prime(number):
            return [number] + get_array_from_number(number-1)
        else:
            return get_array_from_number(number-1)

    return get_array_from_number(n)
