
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
    l1 = lst1.copy()
    l2 = lst2.copy()
    i = 0
    even_index_list = []
    for val in l1:
        if val % 2 == 0:
            even_index_list.append(i)
        i += 1
    for val in even_index_list:
        lst1.pop(val)
    if len(lst1) == 0:
        return "YES"
    else:
        for val in l2:
            if val % 2 != 0:
                lst2.pop(lst2.index(val))
        if len(lst2) == 0:
            return "YES"
        else:
            return "NO"

