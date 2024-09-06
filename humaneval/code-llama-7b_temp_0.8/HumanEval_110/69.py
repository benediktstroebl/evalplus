
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

    # Implicitly bubble sort lists
    # O(n^2) runtime
    # O(1) space

    # temp list to hold all the even numbers
    even_list = []

    # loop through the first list, and append all the even numbers to a list
    for item in lst1:
        if item % 2 == 0:
            even_list.append(item)

    # loop through the second list
    for item in lst2:
        # if the current item is in the even list, remove it from the even list
        if item in even_list:
            even_list.remove(item)

    # if the even list is empty, return yes
    if len(even_list) == 0:
        return "YES"
    else:
        return "NO"

