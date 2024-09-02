
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    assert isinstance(a, int)
    assert 0 < a < 100

    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        j = 5
        while j * j <= num:
            if num % j == 0 or num % (j + 2) == 0:
                return False
            j += 6
        return True
    
    prime_list = []
    for i in range(a):
        if is_prime(i) == True:
            prime_list.append(i)

    if len(prime_list) >= 3:
        for i in prime_list:
            for j in prime_list:
                for k in prime_list:
                    if i * j * k == a:
                        return True
    else:
        return False

