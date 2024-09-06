
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 0:
        return False
    a_str = str(a)
    if len(a_str) == 1:
        return a in [2,3,5,7]
    # get the list of prime numbers
    l = []
    if a_str[0] != '0':
        l.append(2)
    if a_str[1] != '0':
        l.append(3)
    if a_str[1] != '1':
        l.append(5)
    if a_str[0] != '1':
        l.append(7)
    # now check the list
    if len(l) == 0:
        return False
    else:
        for prime in l:
            if a % prime != 0:
                return False
        return True
    
