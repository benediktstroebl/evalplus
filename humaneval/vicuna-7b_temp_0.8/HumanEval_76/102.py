
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Check if n is 1
    if n == 1:
        return x == 1

    # Check if x is equal to n**int
    if x == n**int:
        return True

    # Check if n is even
    if n % 2 == 0:
        # Check if x is even
        if x % 2 == 0:
            return True
        # Check if x is odd
        else:
            return True

    # Check if x is odd
    if x % 2 != 0:
        return True

    # Check if x is greater than n
    if x > n:
        return False

    # Check if x is less than n
    if x < n:
        return False

    # Check if x is a simple power of n
    # You can use Euclid's algorithm to check if x is a simple power of n
    # It is a good idea to implement this function using Euclid's algorithm
    # You can also use the definition of a simple power to check if x is a simple power of n
    # In this case, x is a simple power of n if n**int=x
    # Return True if x is a simple power of n and False otherwise
    return False