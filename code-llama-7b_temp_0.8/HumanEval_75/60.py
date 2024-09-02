
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    lst = []
    for i in range(2, int(a/2)+1):
        if a%i == 0:
            lst.append(i)

    # check if the number of prime numbers is 3
    return (len(lst) == 3)
