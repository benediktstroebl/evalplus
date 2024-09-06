
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a > 100:
        return False
    prime = 0
    for i in range(2,a):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime += 1
            if prime == 3:
                for k in range(2,a):
                    for l in range(2,k):
                        if k % l == 0:
                            break
                    else:
                        return True
    return False


