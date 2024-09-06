
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    for i in range(2, a):
        if a % i == 0:
            print('{} / {} = {}'.format(a, i, a / i))
            if (a / i == 2) and (i % 2!= 0) and (i % 3!= 0) and (i % 5!= 0):
                print('{} = 2 * {} * {} * {}'.format(a, i, a / i, i))
                return True
            elif (a / i == 3) and (i % 2!= 0) and (i % 3!= 0) and (i % 5!= 0):
                print('{} = 3 * {} * {} * {}'.format(a, i, a / i, i))
                return True
            elif (a / i == 5) and (i % 2!= 0) and (i % 3!= 0) and (i % 5!= 0):
                print('{} = 5 * {} * {} * {}'.format(a, i, a / i, i))
                return True
            else:
                return False

