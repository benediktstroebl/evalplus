
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

    # check if the first list contains only odd numbers
    for i in lst1:
        if i % 2 == 0:
            return 'NO'

    # iterate through both lists at the same time
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            if lst2[i] % 2 == 0:
                # exchange odd number in first list with even number in second list
                lst1[i], lst2[i] = lst2[i], lst1[i]
            else:
                # we cannot exchange two odd numbers
                return 'NO'
    # return 'YES' if the first list only contain even numbers
    return 'YES'


