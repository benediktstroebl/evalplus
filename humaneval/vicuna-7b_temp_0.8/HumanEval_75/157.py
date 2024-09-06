
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    is_prime = True
    for i in range(1, a-1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        for i in range(2, int(a**0.5)+1, 2):
            if a % i == 0:
                is_prime = False
                break
    return is_prime