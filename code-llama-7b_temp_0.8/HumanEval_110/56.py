
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
    # YOUR CODE HERE
    # check if all elements in lst1 are even
    # if all([True if not x%2 else False for x in lst1]):
    #     # all elements in lst1 are even
    #     return "YES"
    #
    #
    # # check if all elements in lst2 are odd
    # if all([True if x%2 else False for x in lst2]):
    #     # all elements in lst2 are odd
    #     return "YES"
    #
    #
    # # check if all elements in lst1 are odd
    # if all([True if not x%2 else False for x in lst1]):
    #     # all elements in lst1 are odd
    #     return "NO"
    #
    # # check if all elements in lst2 are even
    # if all([True if x%2 else False for x in lst2]):
    #     # all elements in lst2 are even
    #     return "NO"
    #
    #
    # # check if lst1 and lst2 have the same number of odd elements and even elements
    # if sum([True if not x%2 else False for x in lst1]) == sum([True if x%2 else False for x in lst2]):
    #     return "YES"
    #
    # return "NO"

    # another approach
    # check if all elements in lst1 are even
    if all([True if not x%2 else False for x in lst1]):
        # all elements in lst1 are even
        return "YES"

    # check if all elements in lst2 are odd
    if all([True if x%2 else False for x in lst2]):
        # all elements in lst2 are odd
        return "YES"

    return "NO"

