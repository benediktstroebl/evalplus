
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is divisible by any of the primes 2, 3, and 5
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a % 5 == 0:
        return False
    # Check if the sum of digits of a is divisible by any of the primes 2, 3, and 5
    digits = [str(d) for d in range(10)]
    sum_digits = sum(digits)
    for i in range(2, 6):
        if (sum_digits % i) == 0:
            return False
    # If none of the above conditions are met, it is a multiply prime number
    return True
