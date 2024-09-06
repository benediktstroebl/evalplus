
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    for i in range(2, 100):
        if i == 2:
            j = 2
        if i == 3:
            j = 3
        if i == 5:
            j = 5
        if i == 7:
            j = 7
        if i == 11:
            j = 11
        if i == 13:
            j = 13
        if i == 17:
            j = 17
        if i == 19:
            j = 19
        if i == 23:
            j = 23
        if i == 29:
            j = 29
        if i == 31:
            j = 31
        if i == 37:
            j = 37
        if i == 41:
            j = 41
        if i == 43:
            j = 43
        if i == 47:
            j = 47
        if i == 53:
            j = 53
        if i == 59:
            j = 59
        if i == 61:
            j = 61
        if i == 67:
            j = 67
        if i == 71:
            j = 71
        if i == 73
