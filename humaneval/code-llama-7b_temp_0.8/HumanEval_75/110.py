
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Find 3 prime numbers
    for i in range(2,100):
        for j in range(2,100):
            for k in range(2,100):
                # Check if (i * j * k) = a
                if (i * j * k) == a:
                    # Check if i,j,k are prime numbers
                    if is_prime(i) and is_prime(j) and is_prime(k):
                        return True
    return False
