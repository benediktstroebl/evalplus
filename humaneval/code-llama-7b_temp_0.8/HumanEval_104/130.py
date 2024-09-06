
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # your code here
    # if i try to understand how to do it without convert the number to string, i'm stucked
    # so the first thing i did was to convert the number to string

    # m = []
    # for element in x:
    #     if not '0' in str(element) and not '2' in str(element) and not '4' in str(element) and not '6' in str(element) and not '8' in str(element):
    #         m.append(element)
    # return sorted(m)

    # but i saw in the forum that exists a method to convert a number to a list with the digits of the number
    # so this is my second try

    lista = [int(i) for i in str(x)]

    if 0 in lista and 2 in lista and 4 in lista and 6 in lista and 8 in lista:
        return []
    else:
        return sorted(x)
