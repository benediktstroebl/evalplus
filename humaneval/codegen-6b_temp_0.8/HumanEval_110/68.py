
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
    # You can use the following strategy:
    # take a new list identical to lst1
    # keep only the even elements
    # check if the new list is equal to lst2
    # if so, return "YES"
    # if not, return "NO"
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst2_even = [i for i in lst2 if i % 2 == 0]
    return lst1_even == lst2_even


