
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
    # loop through the lists
    # make a copy of the first list
    # check if the numbers are even if not, return NO
    # remove the value from the first list
    # add the value to the second list
    # return YES
    # will run into a list index out of range error if one of the lists contains a non integer value
    # If the list contain a non integer value, return "NO"

    if type(lst1) is not list or type(lst2) is not list:
        return "NO"
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    if len(lst1) > len(lst2):
        return "NO"

    new_lst1 = lst1.copy()
    for x in lst1:
        if x % 2 != 0:
            return "NO"
    for y in lst1:
        lst2.append(y)
        lst1.remove(y)
    return "YES"

