
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        i = 2
        prime = []
        while i < a:
            j = 2
            status = True
            while j != i and status == True:
                if i%j == 0:
                    status = False
                else:
                    j += 1
            if status == True:
                prime.append(i)
            i += 1
        status = True
        for i in prime:
            if a % i != 0:
                status = False
        if status == True:
            return True
        return False
    return False
