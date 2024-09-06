
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
    # create a copy of the input lists
    lst1 = [x for x in lst1]
    lst2 = [x for x in lst2]
    
    # check if all the elements of lst1 are even
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    
    # check if all the elements of lst2 are odd
    if all(x % 2 == 1 for x in lst2):
        return "YES"
    
    # check if there is any common element in lst1 and lst2
    if any(x in lst2 for x in lst1):
        return "YES"
    
    return "NO"
