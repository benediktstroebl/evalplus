
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # create dict to store cache values
    cache = {}

    # initialize return value
    return_val = False

    # check if x and n are already in the cache
    if x in cache:
        return_val = cache[x]

    # check if both x and n are in the cache
    if n in cache:
        return_val = cache[x] and cache[n]

    # x is in the cache and n is not in the cache
    # simplify x
    if x in cache and not n in cache:
        return_val = True
        result = simplify(x, 1)
        if result:
            cache[x] = True
            cache[result] = True
            return return_val

    # n is in the cache and x is not in the cache
    # simplify n
    if n in cache and not x in cache:
        return_val = True
        result = simplify(n, 1)
        if result:
            cache[n] = True
            return return_val

    # both x and n are not in the cache
    # check if x and n are integers
    if x.isdigit() and n.isdigit():
        # convert x and n to int
        x = int(x)
        n = int(n)
        if x == n or (x+1) == n:
            # if x and n are integers and x is not zero, they are equal
            return_val = True
        else:
            # otherwise, they are not equal
            return_val = False
    else:
        return_val = False

    # if x and n are not integers, check if they are whole numbers
    if x.isdigit() or n.isdigit():
        # if they are not integers, check if they are whole numbers
        if x.isdigit() and n.isdigit() and (x+1).isdigit() and (n+1).isdigit():
            # convert x and n to float
            x = float(x)
            n = float(n)
            # check if x and n are equal
            if x == n or (x+1) == n:
                # if x and n are
