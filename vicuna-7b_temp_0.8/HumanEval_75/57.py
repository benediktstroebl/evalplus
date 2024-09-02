
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i = 2
    for num in range(a, 100, 2):
        if is_prime(num) != True:
            return False
        if num % 2 == 0:
            continue
        while i <= a:
            if is_prime(num * i) == False:
                break
            i += 1
        if i > a:
            return False
    return True