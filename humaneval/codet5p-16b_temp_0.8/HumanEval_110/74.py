
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

    lst1.sort()
    lst2.sort()
    index1 = 0
    index2 = 0
    for index in range(len(lst1)):
        if lst1[index] % 2!= 0:
            break
        index1 = index
    for index in range(len(lst2)):
        if lst2[index] % 2!= 0:
            break
        index2 = index
    if index1!= index2:
        return "NO"
    if index1 == len(lst1) - 1 and index2 == len(lst2) - 1:
        return "NO"
    if index1 == index2:
        if index2 == len(lst2) - 1 and index1 < len(lst1) - 1:
            if lst1[index1 + 1] % 2 == 0:
                return "YES"
    if index1 < len(lst1) - 1 and index2 == len(lst2) - 1:
        if lst1[index1 + 1] % 2 == 0:
            return "
