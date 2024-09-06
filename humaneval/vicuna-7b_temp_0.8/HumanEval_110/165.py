
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
    # checking whether the two lists are same or not
    if lst1 == lst2:
        return "YES"
    # checking whether all the elements of lst1 are odd or even
    if not all(lst1[1:] % 2 == 0 for lst1 in lst1):
        return "YES"
    # checking whether all the elements of lst2 are odd or even
    if not all(lst2[1:] % 2 == 0 for lst2 in lst2):
        return "YES"
    # if it is not possible to make all elements of lst1 to be even,
    # then it is not possible to exchange elements between the two lists
    return "NO"
