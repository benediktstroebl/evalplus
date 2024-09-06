
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        my_list = [2,3,5,7]
        for n in my_list:
            if a%n == 0:
                a = a/n
                print(a)
                if a == 1:
                    return True
        return False
    return False
