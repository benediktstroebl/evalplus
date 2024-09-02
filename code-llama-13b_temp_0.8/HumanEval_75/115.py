
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(num):
        if num == 1:
            return False
        if num < 4:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num**0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True

    result = []
    for i in range(1, 100):
        if is_prime(i):
            result.append(i)
    res_2 = []
    for i in result:
        if is_prime(a / i):
            res_2.append(i)
    res_3 = []
    for i in res_2:
        if is_prime(a / i / i):
            res_3.append(i)
    if len(res_3) > 0:
        return True
    else:
        return False

