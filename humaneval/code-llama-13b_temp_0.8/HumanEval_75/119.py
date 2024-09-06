
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_multiply = False
    for a in range(2, 100):
        prime = [2, 3, 5, 7]
        if a % prime[0] == 0 and a % prime[1] == 0 and a % prime[2] == 0 and a % prime[3] == 0:
            is_multiply = True
            break
        else:
            is_multiply = False
    return is_multiply

