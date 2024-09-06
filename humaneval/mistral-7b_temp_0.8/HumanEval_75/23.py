
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    """ 1st solution: O(n) """
    def helper(num):
        if num == 1:
            return True
        elif num < 3:
            return False
        else:
            for i in range(3, num):
                if num % i == 0:
                    return False
                else:
                    continue
            return True

    # Solution 2
    def is_prime(n):
        # Check if n is 1 or 2
        if n < 2:
            return False
        # Check if n is a prime number
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return (helper(a))


