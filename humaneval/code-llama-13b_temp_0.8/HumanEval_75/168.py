
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2, a // 2):
        if i * i > a:
            break
        if a % i == 0:
            for j in range(2, i // 2):
                if j * j > i:
                    break
                if i % j == 0:
                    return False
    return True
