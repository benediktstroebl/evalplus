
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
    #
    # initialize an empty list to store the results
    #
    results = []
    #
    # check if n is 0 or 1, if so return an empty list
    #
    if n == 0 or n == 1:
        return []
    #
    # check if n is prime
    #
    if n % 2 == 0:
        return []
    #
    # check if n is less than or equal to 3
    #
    if n <= 3:
        return [n]
    #
    # check if n is less than or equal to the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # otherwise, check if n is less than or equal to the square root of the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # check if n is less than or equal to the square root of the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # check if n is less than or equal to the square root of the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # otherwise, check if n is less than or equal to the square root of the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # check if n is less than or equal to the square root of the square root of n
    #
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return []
    #
    # check if
