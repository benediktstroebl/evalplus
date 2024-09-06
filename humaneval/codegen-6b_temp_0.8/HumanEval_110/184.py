
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

    ind1, ind2 = 0, 0
    while ind1 < len(lst1) and ind2 < len(lst2):
        if lst1[ind1] % 2 == 1 and lst2[ind2] % 2 == 0 and ind1 < ind2:
            return "NO"
        elif lst1[ind1] % 2 == 0 and lst2[ind2] % 2 == 1:
            return "NO"
        elif lst1[ind1] % 2 == 1 and lst2[ind2] % 2 == 1:
            lst1[ind1], lst2[ind2] = lst2[ind2], lst1[ind1]
            ind1 += 1
            ind2 += 1
        elif lst1[ind1] % 2 == 1:
            ind1 += 1
        else:
            ind2 += 1

    return "YES"

