
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
    # check if all elements of lst1 are even, if they are return "YES"
    if all([elem % 2 == 0 for elem in lst1]):
        return "YES"
    # if not create a list of all even elements in lst2
    # if the length of this list is equal to the length of lst1,
    # then return "YES"
    # otherwise return "NO"
    else:
        evens = [elem for elem in lst2 if elem % 2 == 0]
        if len(evens) == len(lst1):
            return "YES"
        else:
            return "NO"
