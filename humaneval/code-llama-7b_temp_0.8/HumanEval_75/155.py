
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        for i in range(3, 100):
            if a % i != 0:
                continue
            for j in range(3, 100):
                if i % j != 0:
                    continue
                for k in range(3, 100):
                    if k % j != 0 and k % i != 0:
                        return a == k * j * i
    return False
    
