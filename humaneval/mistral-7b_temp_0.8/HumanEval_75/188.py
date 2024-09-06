
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # a = int(input())
    if a == 1:
        return False
    i = 3
    while i <= a:
        if i ** 2 > a:
            break
        else:
            j = i
            while j <= a:
                if a % j == 0:
                    if j == 2 or j == 3:
                        return True
                    else:
                        return False
                j += 1
        i += 2
    return False
