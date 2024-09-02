
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    if not lst1 or not lst2:
        return "NO"

    if len(lst1) == 1:
        if lst1[0] % 2 == 0:
            return "YES"

    if lst1[-1] % 2 == 0:
        return "YES"

    # 0-1: check if one of the lists is all even numbers
    # check if lst1[0] is even
    if lst1[0] % 2 == 0:
        # check if lst2[-1] is even
        if lst2[-1] % 2 == 0:
            # check if lst2[-1] is in lst1
            if lst2[-1] in lst1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

    # 0-2: check if the last number in lst1 is even
    if lst1[-1] % 2 == 0:
        # check if lst2[0] is even
        if lst2[0] % 2 == 0:
            # check if lst1[-1] is in lst2
            if lst1[-1] in lst2:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

    return "NO"

