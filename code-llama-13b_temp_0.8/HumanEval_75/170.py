
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    number = a
    list_number = []
    while number > 1:
        for prime in prime_list:
            if number % prime == 0:
                list_number.append(prime)
                number = number / prime
    return sorted(list_number) == [2, 3, 5]

