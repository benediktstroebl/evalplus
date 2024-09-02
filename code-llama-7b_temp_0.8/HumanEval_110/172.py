
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
    # To hold the values that will be swapped
    temp = []
    # To hold the values that will remain unchanged
    final = []

    for x in lst1:
        if x % 2 == 0:
            final.append(x)
        else:
            temp.append(x)

    for y in lst2:
        if y % 2 == 0:
            final.append(y)
        else:
            temp.append(y)

    # If the lists are equal, then the function can return YES
    if lst1 == lst2:
        return "YES"
    # If there are no even numbers in the lists, then the function can return NO
    if len(final) == 0:
        return "NO"
    # If the lists are not equal and there are even numbers,
    # then the function can return YES
    if len(final) != 0 and lst1 != lst2:
        return "YES"

