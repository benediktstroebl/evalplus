
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                return False
        return True

    def is_multiple(a):
        for b in range(2, int(a ** 0.5) + 1):
            for c in range(2, int(b ** 0.5) + 1):
                if a % (b * c) == 0:
                    return True
        return False

    a = int(input("Enter a number to check: "))
    if is_prime(a) or is_multiple(a):
        return False
    elif a > 3:
        for i in range(2, int(a ** 0.5) + 1):
            if is_prime(a // i) and is_prime(i) and (a // i) != i:
                return True
        return False
    else:
        return True

a = is_multiply_prime(30)
