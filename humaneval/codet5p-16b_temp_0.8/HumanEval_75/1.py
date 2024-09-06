
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    
    
    for i in range(1,101):
        if i % 3 == 0 and i % 2!= 0:
            for j in range(1,101):
                if j % 2!= 0 and j % 3!= 0:
                    if a == i * j:
                        return True
                    else:
                        return False
        else:
            continue
