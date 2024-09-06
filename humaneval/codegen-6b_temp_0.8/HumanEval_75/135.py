
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    count = 0
    limit = 11
    number = a
    while count < limit:
        number = number + 2
        prime = True
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                prime = False
                break
        if prime == True:
            count = count + 1
    if count < limit:
        return True
    else:
        return False
