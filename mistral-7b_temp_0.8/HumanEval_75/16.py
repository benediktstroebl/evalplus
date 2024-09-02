
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    #TODO: Write the function below
    def is_prime(x):
        if x < 3:
            return False
        elif x == 3:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True

    def is_multiply_prime(a):
        return is_prime(a) and a % 2 == 0

    return is_multiply_prime(a)



