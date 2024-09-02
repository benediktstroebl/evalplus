

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    # hint 1: this function is already implemented (as "all")
    # hint 2: you can use the "lt" function

    # insert solution here

    return all(lt(l[i], t) for i in range(len(l)))
