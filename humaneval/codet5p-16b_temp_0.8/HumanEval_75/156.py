
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    result = False
    for i in range(2, a):
        if a % i == 0:
            j = i + 1
            while j <= a / i:
                if j % i == 0:
                    result = True
                    break
                j += 1
            if result:
                break
    return result

