
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(number):
        if number < 2:
            return False
        if number == 2:
            return True
        for x in range(2, number):
            if number % x == 0:
                return False
        return True
    def is_prime_pair(number):
        x = 2
        count = 0
        while x <= number:
            if number % x == 0:
                return False
            x += 1
            count += 1
        if count == 2:
            return True
        return False
    def is_multiply_prime(number):
        result = False
        for x in range(2, number + 1):
            if is_prime_pair(x) and is_prime(number / x):
                return True
        return result
    return is_multiply_prime(a)
