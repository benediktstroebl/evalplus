
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for x in range(1, 100):
        if a % x!= 0:
            continue
        for y in range(1, 100):
            if a % y!= 0:
                continue
            for z in range(1, 100):
                if a % z!= 0:
                    continue
                if x == y or x == z or y == z:
                    continue
                if x * y * z == a:
                    return True
    return False

