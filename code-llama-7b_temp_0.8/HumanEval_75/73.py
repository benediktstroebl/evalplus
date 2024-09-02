
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = [2,3,5,7,11,13,17,19,23,29]
    for prime_num in prime_list:
        if a%prime_num == 0:
            print(prime_num)
            if a == prime_num:
                return True
            elif a == prime_num*prime_num:
                return True
            elif a == prime_num*prime_num*prime_num:
                return True
            else:
                return False
        else:
            return False




