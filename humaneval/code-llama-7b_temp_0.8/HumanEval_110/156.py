
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
    # create a new list
    # compare the values in the list to the target number
    # if the values are the target number, switch them
    # if any values are not the target number, return no
    # when all the values are the target number, return yes
    if len(lst1) != len(lst2):
        return "NO"
    # Create a new empty list
    newList = []
    # Check each value in the first list, if it is the target number, append it to the new list
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            newList.append(lst1[i])
        else:
            return "NO"

    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            newList.append(lst2[i])
        else:
            return "NO"

    return "YES"

