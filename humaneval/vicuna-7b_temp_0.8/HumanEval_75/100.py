
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Your code here
    for i in range(2, a):
        for j in range(2, a-i+1):
            if (a % i) == 0:
                for k in range(i+1, a):
                    if (a % k) == 0:
                        return False
                return True
    return True