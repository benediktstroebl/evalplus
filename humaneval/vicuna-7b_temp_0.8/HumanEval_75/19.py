
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Initialize variables
    count = 0
    for x in range(a):
        if (a % x) == 0:
            count += 1
    if count > 1:
        return False
    else:
        for i in range(2, int(a/2)+1):
            if (a % i) == 0:
                count += 1
        if count > 1:
            return False
        else:
            for j in range(2, int(a/2)+1):
                for k in range(2, int(a/2)+1):
                    if (a % (j * k)) == 0:
                        count += 1
                if count > 1:
                    return False
                else:
                    return True
