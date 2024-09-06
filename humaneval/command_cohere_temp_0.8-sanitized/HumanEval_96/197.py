def count_up_to(n):
    # check if n is 0 or 1, in that case return an empty list
    if n < 2:
        return []
    # initialize a list to store the prime numbers and an iterator
    result = []
    iterator = 2
    while len(result) < n:
        # iterate through integers 2, 3, 4, ... until we reach n
        iterator += 1
        # check if the iterator is a prime number and it is less than n
        if is_prime(iterator) and iterator < n:
            result.append(iterator)
    # return the list of prime numbers less than n
    return result
def is_prime(n):
    # check if n is less than or equal to 1, in that case return False
    if n <= 1:
        return False
    # check if n is 2 or 3, in that case return True
    if n <= 3:
        return True
    # check if n is divisible by 2 or 3, in that case return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    # check divisibility by all numbers of the form 6k + (-)1, 6k + 1, 6k + 2, 6k + 3, ...
    # corresponding to all possible remainders from dividing n by 6
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    # if none of the conditions for non-prime numbers is satisfied, return True
    return True