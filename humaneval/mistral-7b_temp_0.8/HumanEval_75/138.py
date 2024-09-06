
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # first of all we need to get the prime factors of a
    factors = [2]
    factor = 3
    # this is done by a while loop
    while factor * factor <= a:
        # here we need to check if the factor is prime or not
        # the prime number is the number that has two factors 1 and itself
        # we can do this by dividing the number with the current factor
        # if the remainder is 0 then the number is not prime
        # if the remainder is not zero then the number is prime
        while a % factor == 0:
            factors.append(factor)
            a = a/factor
        factor += 2
    # if the factor is greater than the square root of a,
    # we can stop the loop
    if factor > a**0.5:
        factors.append(a)
    # this means we have the prime factors of a
    # now we need to check if the size of the factors is 3 or not
    if len(factors) != 3:
        return False
    else:
        return True
