
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a % 2 == 0:
        return False
    return a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 23 or a == 29 or a == 31 or a == 37 or a == 41 or a == 43 or a == 47 or a == 53 or a == 59 or a == 61 or a == 67 or a == 71 or a == 73 or a == 79 or a == 83 or a == 89 or a == 97 or a == 101 or a == 103 or a == 107 or a == 109 or a == 113 or a == 127 or a == 131 or a == 137 or a == 139 or a == 149 or a == 151 or a == 157 or a == 163 or
