
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
    """
    lst1 = []
    lst2 = []
    while lst1 != []:
        max_element = max(lst1)
        if max_element % 2 == 0:
            lst1.remove(max_element)
            lst2.append(max_element)
        else:
            return "NO"
    while lst2 != []:
        max_element = max(lst2)
        if max_element % 2 == 0:
            lst2.remove(max_element)
            lst1.append(max_element)
        else:
            return "NO"
    return "YES"
    """

    lst1 = []
    lst2 = []
    while lst1 != []:
        max_element = max(lst1)
        if max_element % 2 == 0:
            lst1.remove(max_element)
            lst2.append(max_element)
        else:
            return "NO"
    while lst2 != []:
        max_element = max(lst2)
        if max_element % 2 == 0:
            lst2.remove(max_element)
            lst1.append(max_element)
        else:
            return "NO"
    return "YES"

