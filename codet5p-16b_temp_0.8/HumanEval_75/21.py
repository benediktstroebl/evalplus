
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a < 100:
        for i in range(3, a):
            if a % i!= 0:
                continue
            else:
                i = a / i
                for j in range(3, int(i)):
                    if i % j!= 0:
                        continue
                    else:
                        j = int(i / j)
                        for k in range(3, int(j)):
                            if j % k!= 0:
                                continue
                            else:
                                k = int(j / k)
                                return True
    else:
        return False
    
