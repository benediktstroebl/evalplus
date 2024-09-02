
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # result = False
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # for prime in primes:
    #     for prime_number in primes:
    #         if prime * prime_number == a:
    #             result = True
    #             break
    # return result
    # You can optimize the above program by using a dictionary to store the multiples of prime numbers.
    result = False
    primes = {2: 2, 3: 3, 5: 5, 7: 7, 11: 11, 13: 13, 17: 17, 19: 19, 23: 23, 29: 29}
    for prime in primes:
        for prime_number in primes:
            if prime * prime_number == a:
                result = True
                break
    return result


