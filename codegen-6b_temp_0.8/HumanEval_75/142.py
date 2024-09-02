
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    skip = [] # skip[i] is True if the number is multipliable by j
    for i in range(2, a + 1):
        if skip[i] == 1:
            continue

        remainder = a % i
        if remainder == 0:
            return False

        for j in range(2, int(a ** .5) + 1):
            if i * j > a:
                break

            if remainder % j == 0:
                skip[i * j] = 1
                skip[i] = 1
                break
    return True

