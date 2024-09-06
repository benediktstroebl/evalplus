
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a == 3:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                prime = False
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        prime = True
                        break
                if prime == False:
                    return True
    return False
