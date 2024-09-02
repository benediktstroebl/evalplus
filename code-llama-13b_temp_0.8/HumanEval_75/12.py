
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        is_prime = [True for i in range(101)]
        i = 2
        while i <= 100:
            j = 2
            while i * j <= 100:
                is_prime[i * j] = False
                j += 1
            i += 1
        counter = 0
        for i in range(2, int(a / 2) + 1):
            if is_prime[i]:
                if a % i == 0:
                    counter += 1
                    if counter == 3:
                        return True
    return False
