
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    for i in range(2,100):
        is_prime = True
        if i != 1:
            for k in range(2,i):
                if k != 1:
                    if i%k == 0:
                        is_prime = False
                        break
            if is_prime:
                prime_list.append(i)
    for i in prime_list:
        if a == i:
            return True
    return False
