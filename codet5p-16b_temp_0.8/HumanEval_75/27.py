
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    a = int(a)
    divisors = []
    for i in range(2,a):
        if a % i == 0:
            divisors.append(i)
    if len(divisors) < 3:
        return False
    else:
        for j in range(0,len(divisors)):
            for k in range(j+1,len(divisors)):
                if divisors[j]!= divisors[k]:
                    if (divisors[j] * divisors[k]) == a:
                        return True
    return False
















