
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

    # convert the numbers to float
    n = float(n)
    x = float(x)
    # if the numbers are the same the return True
    if x == n:
        return True
    # check if n is a multiple of x
    # the problem doesn't give any info about the numbers
    # so if the number is a multiple it could be either n or x
    if n % x == 0:
        # calculate the result of n to the power of x
        result = n**(1/x)
        # convert the result to int because we are comparing it with an int
        result = int(result)
        # check if the result is equal to x
        if result == x:
            return True
        else:
            return False
    else:
        # otherwise return False
        return False
