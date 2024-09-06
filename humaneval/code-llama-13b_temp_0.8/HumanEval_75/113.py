
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    import math
    n = math.floor(math.sqrt(a))
    prime_list = []
    for x in range(2, n+1):
        flag = True
        for y in prime_list:
            if x % y == 0:
                flag = False
                break
        if flag:
            prime_list.append(x)
    for x in prime_list:
        if a % x != 0:
            return False
    return True
