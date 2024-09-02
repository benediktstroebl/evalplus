
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = []
    to_check = 2
    while len(primes) < 3:
        # add to_check to list of primes
        if to_check % 2 == 0:
            to_check += 1
        elif is_prime(to_check):
            primes.append(to_check)
            to_check += 1
        else:
            to_check += 1

    if a % primes[0] == 0 and a % primes[1] == 0 and a % primes[2] == 0:
        return True
    else:
        return False

