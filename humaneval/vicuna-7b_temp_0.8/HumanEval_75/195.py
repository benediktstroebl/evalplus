
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # create a list of prime numbers less than a
    prime_numbers = [x for x in range(1, int(a**0.5) + 1) if x % 2 == 1]
    # check if the number is the multiplication of the prime numbers
    for i in range(3, len(prime_numbers)):
        if a % prime_numbers[i] == 0:
            return False
    return True
