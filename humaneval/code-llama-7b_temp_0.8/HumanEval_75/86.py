
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a<2:
        return False
    prime = [2, 3, 5]
    flag = False
    for i in range(len(prime)):
        for j in range(i+1, len(prime)):
            for k in range(j+1, len(prime)):
                if prime[i]*prime[j]*prime[k]==a:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    return flag
