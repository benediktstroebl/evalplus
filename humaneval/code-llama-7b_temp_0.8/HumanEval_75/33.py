
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if not isinstance(a, int) or a > 100:
        raise ValueError('a is not integer or is bigger than 100')
    
    if a == 2 or a == 3 or a == 5:
        return True

    if a%2 == 0 or a%3 == 0 or a%5 == 0:
        return False

    prime_list = [2,3,5]
    while prime_list[-1] * prime_list[-1] < a:
        for p in prime_list:
            if a % p == 0:
                break
        else:
            prime_list.append(int(a/prime_list[-1]))
            continue
        break
    
    if prime_list[-1] * prime_list[-1] == a:
        return True
    else:
        return False
