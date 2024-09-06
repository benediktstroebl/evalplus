
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def check_divisor(n, x):
        for i in range(x):
            if n % i == 0:
                return False
        return True
    if check_divisor(a, 2) or check_divisor(a, 3) or check_divisor(a, 5):
        return False
    for i in range(3, int(a**0.5) + 1, 2):
        j = 2
        while j * j <= i:
            if is_prime(i - j * j):
                a = i
                break
            j += 1
        if a is not None:
            break
    return True
