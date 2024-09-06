
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
    # good luck with this one.
    # it should be easy, just loop through both lists and compare
    # if the two don't have the same length, return no.
    # and if all of the elements of lst1 are even, return yes
    # there will be some work in the if statement, so it will be
    # best to break it up into pieces
    if len(lst1) != len(lst2):
        return "NO"
    else:
        if all(x % 2 == 0 for x in lst1):
            return "YES"
        else:
            return "NO"
