
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Base case:
    if a < 100:
        if a == 2 * 3 * 5:
            return True
        else:
            return False
    # General case:
    else:
        # We know that the number of factors of 2 is less then the number of its own factors:
        # a_2 <= a_f
        # Thus, we only need to check the factors of 2, till the number of its own factors (a_f):
        a_f = round(a / 2)  # number of factors
        for i in range(2, a_f + 1):
            # Check if the number is divisible by 2 and to which power:
            # If the number is divisible by 2 and to power 1:
            # The power is the number of 2's in the number of its factors.
            # Thus, if it is divisible by 2 and to power 1, the power is 1.
            if a % i == 0:
                # We know that the number of factors of 3 is less then the number of its own factors:
                # a_3 <= a_f
                # Thus, we only need to check the factors of 3, till the number of its own factors (a_f):
                a_3 = round(a / 3)  # number of factors
                for j in range(2, a_3 + 1):
                    # Check if the number is divisible by 3 and to which power:
                    # If the number is divisible by 3 and to power 1:
                    # The power is the number of 3's in the number of its factors.
                    # Thus, if it is divisible by 3 and to power 1, the power is 1.
                    if a % j == 0:
                        # We know that the number of factors of 5 is less then the number of its own factors:
                        # a_5 <= a_f
                        # Thus, we only need to check the factors of 5, till the number of its own factors (a_f):
                        a_5 = round(a / 5)  # number of factors
