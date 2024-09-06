
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Loop over all numbers from 3 to 100
    for i in range(3, 100):
        if (i % 6 != 0 and i % 3 != 0):
            # If i is divisible by 6 or 3, it's not a multiply prime
            if i % 2 == 0:
                # If i is even, it can't be a multiply prime
                continue
            # If i is not divisible by 6 or 3, it is a multiply prime
            if a % i == 0:
                # If a is divisible by i, it's not a multiply prime
                return False
    # If no condition is met, the number is multiply prime
    return True


    # My second solution, even from an earlier challenge.
    # SAME TECHNIQUE:
    # Loop over numbers from 3 to 100
    # If the number is divisible by 2, iterate through all prime numbers
    # if the given number is divisible by the number, return false
    # Continue to the next number, following the pattern of 
    # 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, ...
    # when the number can be evenly divided by a number, it is not a multiply prime
    # A number is divisible by (x) if it is evenly divisible by ALL prime numbers from 2 up to x
    # 5 = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 49, 53, 59, 61, 67, 71, 73, 79
    # 10 = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 47, 53, 59, 61, 67, 71, 73, 79
    # 15 = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 47, 53, 59, 61, 67, 71, 73, 79
    # Return true if it is multiply prime, false if it is not