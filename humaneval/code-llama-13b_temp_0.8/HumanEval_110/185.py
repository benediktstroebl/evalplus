
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

    # we will try to empty lst1, so we will just go through lst2
    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            lst1.append(lst2[i])
        else:
            lst2[i] = 0

    # check if we managed to empty lst1
    for i in range(len(lst1)):
        if lst1[i] % 2 == 1:
            return "NO"

    # if we got here, then we managed to empty lst1, so we return "YES"
    return "YES"
