
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        p = []
        prime = True
        for i in range(2, a + 1):
            for j in range(2, i):
                if i % j == 0 and i != j:
                    prime = False
                    break
            if prime:
                p.append(i)
            prime = True
        for i in p:
            for j in p:
                for k in p:
                    if (i * j * k == a):
                        return True
        return False
    else:
        return False
        
