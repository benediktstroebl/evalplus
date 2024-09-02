
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    for i in range(2,a):
        if a % i!= 0:
            continue
        for j in range(2,i+1):
            if i % j!= 0:
                continue
            for k in range(2,j+1):
                if j % k!= 0:
                    continue
                if k == j:
                    return True
    return False

