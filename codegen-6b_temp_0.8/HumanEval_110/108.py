
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
    e_lst1 = lst1[:]
    e_lst2 = lst2[:]
    i = 0
    while e_lst1 and e_lst2:
        if e_lst1[i] % 2 == 0 and e_lst2[i] % 2 == 0:
            e_lst1[i], e_lst2[i] = e_lst2[i], e_lst1[i]
        elif e_lst1[i] % 2 == 0 and e_lst2[i] % 2 != 0:
            e_lst1[i] = e_lst1[i] - 1
            e_lst2[i] = e_lst2[i] + 1
        elif e_lst1[i] % 2 != 0 and e_lst2[i] % 2 == 0:
            e_lst1[i] = e_lst1[i] + 1
            e_lst2[i] = e_lst2[i] - 1
        else:
            e_lst1[i] = e_lst1[i] - 1
            e_lst2[i] = e_lst2[i] - 1
        i += 1
    if not e_lst1 or not e_lst2:
        return "NO"
    else:
        return "YES"

