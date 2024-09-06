
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
    # initialize empty list
    prime_numbers = []
    # check for 0
    if n == 0:
        return prime_numbers
    # check for 1
    elif n == 1:
        return []
    # check for even number
    elif n % 2 == 0:
        return []
    # check for odd number
    else:
        # check for prime numbers less than n
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                continue
            if x % 2 == 0:
                continue
            prime_numbers.append(x)
        return prime_numbers
