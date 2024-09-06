
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

    # a list to keep the prime numbers
    prime_numbers = []

    # if n is not positive, return empty list
    if n <= 1:
        return prime_numbers

    # iterate over the integers from 2 to n
    for integer in range(2, n + 1):
        # check if the integer is prime number
        is_prime_number = True
        for j in range(2, integer):
            if integer % j == 0:
                is_prime_number = False
                break
        if is_prime_number:
            prime_numbers.append(integer)

    return prime_numbers

