
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    list_3 = []
    for i in range(2, 100):
        if not is_prime(i):
            continue
        else:
            list_3.append(i)
    for n in list_3:
        if a % n != 0:
            continue
        else:
            list_4 = []
            for m in list_3:
                if m % n != 0:
                    continue
                else:
                    list_4.append(m)
            for i in list_4:
                if a / i == i:
                    return True
    return False

