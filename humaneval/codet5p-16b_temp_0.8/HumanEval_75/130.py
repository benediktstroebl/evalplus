
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a < 100:
        b = 2
        while b < a:
            if a%b == 0:
                c = 2
                while c < a:
                    if b*c == a:
                        return True
                    c += 1
            b += 1
        return False
    else:
        return False



