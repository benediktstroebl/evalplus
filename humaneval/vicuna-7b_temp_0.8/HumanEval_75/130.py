
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = int(input("Enter a number: "))
    if a < 100:
        for i in range(2, a):
            for j in range(2, i):
                if (a % (i * j)) == 0:
                    return False
        return True
    else:
        return False
