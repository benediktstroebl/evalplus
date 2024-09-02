
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    count = 0
    temp = a
    for i in range(2, int(a**0.5) + 1):
        while temp % i == 0:
            count += 1
            temp //= i
        if count >= 3:
            return False
    return count == 2
