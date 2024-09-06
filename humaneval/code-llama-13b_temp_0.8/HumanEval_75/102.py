
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = [2, 3, 5, 7]
    for i in range(4):
        for j in range(i + 1, 4):
            if prime_numbers[i] * prime_numbers[j] == a:
                return True
    return False

