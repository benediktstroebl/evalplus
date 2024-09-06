
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    """
    My Solution
    """
    prime = []
    for i in range(2, int(a/2)):
        if a%i == 0:
            prime.append(i)
            print(prime)

    if prime == []:
        return True
    else:
        return False


    """
    Official Solution
    """

    return all(any(i for i in prime) for prime in [range(2, n // 2), range(n // 2 + 1, n)] )
