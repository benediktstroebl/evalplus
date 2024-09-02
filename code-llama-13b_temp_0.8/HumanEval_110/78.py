
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
    index1 = 0
    index2 = 0
    while index1 < len(lst1) and index2 < len(lst2):
        # index1-th number of lst1 is even
        if lst1[index1] % 2 == 0:
            index1 += 1
            continue
        # index2-th number of lst2 is even
        if lst2[index2] % 2 == 0:
            index2 += 1
            continue
        # lst1[index1] is odd and lst2[index2] is odd, so we can't change lst1
        if index1 == index2:
            return "NO"
        else:
            # swap lst1[index1] and lst2[index2]
            lst1[index1], lst2[index2] = lst2[index2], lst1[index1]
            index1 += 1
            index2 += 1
    return "YES"

