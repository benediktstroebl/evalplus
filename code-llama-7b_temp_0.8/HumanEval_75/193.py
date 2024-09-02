
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(a):
        if a == 2 or a == 3:
            return True
        elif a < 2 or a%2 == 0 or a%3 == 0:
            return False
        else:
            for i in range(2, int(a ** 0.5) + 1):
                if a%i == 0:
                    return False
            return True
    
    if a < 100:
        num = 1
        count = 0
        while num < a:
            if is_prime(num) and is_prime(a//num):
                count += 1
                if count == 3:
                    return True
            num += 1
    return False
