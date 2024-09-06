
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    return (len(list(filter(lambda n:n%a == 0,range(3,101)))) > 0 and len(list(filter(lambda n:n%a == 0,range(5,101)))) > 0)




