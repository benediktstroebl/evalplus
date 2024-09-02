
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    a = int(input("Enter a positive integer less than 100: "))
    if is_prime(a) == False:
        return False
    b = a - 1
    result = True
    while b >= 3:
        if is_prime(b) == False:
            break
        b = b - 2
        if is_prime(b) == False:
            result = False
        else:
            result = True
    return result
