
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i = 2
    while i * i <= a:
        if a % i == 0:
            k = 2
            j = i * i
            while j != a and j % k == 0:
                k += 1
                j *= i
            if j == a:
                return True
        i += 1
    return False

