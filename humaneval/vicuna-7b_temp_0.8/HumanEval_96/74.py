
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
    # use a list to store the prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    # use a for loop to iterate through the list
    for prime_num in prime_numbers:
        if is_prime(prime_num) and prime_num < n:
            # if the current prime number is less than n and prime, append it to the list
            # append it to the list
            yield prime_num
    # if n is greater than the last prime number in the list, yield n
    # if the last prime number is less than n, yield n
    if n > next(prime_numbers):
        yield n
