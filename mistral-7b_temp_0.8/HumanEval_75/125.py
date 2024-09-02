
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if (a < 1):
        return "number less than 1"
    elif (a == 1):
        return "1 is not a prime number"
    elif (a < 4):
        return "number is not a multiply of 3 prime numbers"

    for i in range(2, a):
        if (a % i == 0):
            return "number is not a multiply of 3 prime numbers"

    return "number is a multiply of 3 prime numbers"

