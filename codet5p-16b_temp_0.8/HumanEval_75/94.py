
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    counter = 0
    while True:
        if a % 3 == 0:
            counter += 1
            a = a / 3
            continue
        else:
            break
    counter += 1
    while True:
        if a % 2 == 0:
            counter += 1
            a = a / 2
            continue
        else:
            break
    counter += 1
    while True:
        if a % 5 == 0:
            counter += 1
            a = a / 5
            continue
        else:
            break
    return counter == 3
