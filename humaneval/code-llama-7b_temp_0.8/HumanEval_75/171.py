
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    a_factors = []
    for i in range(2,a):
        if a%i == 0:
            a_factors.append(i)
    for i in range(len(a_factors)):
        if is_prime(a_factors[i]) == True:
            for j in range(i+1,len(a_factors)):
                if is_prime(a_factors[j]) == True:
                    for k in range(j+1,len(a_factors)):
                        if is_prime(a_factors[k]) == True:
                            if a == a_factors[i] * a_factors[j] * a_factors[k]:
                                return True
    return False

