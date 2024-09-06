
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Given number: {a} is multiply of 3 prime numbers")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    import math

    if a < 1:
        return False
    elif a < 10:
        return False
    elif a < 100:
        if (a % 3 == 0) and (a % 5 == 0) and (a % 7 == 0):
            return True
        else:
            return False
    else:
        for i in range(1, int(math.sqrt(a) + 1)):
            if a % i == 0:
                return True
        return False


