
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
    ix_lst1 = 0
    ix_lst2 = 0
    while ix_lst1 < len(lst1) and ix_lst2 < len(lst2):
        if lst1[ix_lst1] % 2 == 0 and lst2[ix_lst2] % 2 == 0:
            ix_lst1 += 1
            ix_lst2 += 1
        elif lst1[ix_lst1] % 2 != 0 and lst2[ix_lst2] % 2 != 0:
            ix_lst1 += 1
            ix_lst2 += 1
        elif lst1[ix_lst1] % 2 != 0 and lst2[ix_lst2] % 2 == 0:
            ix_lst1 += 1
        else:
            ix_lst2 += 1
    if ix_lst1 < len(lst1) and ix_lst2 < len(lst2):
        return "NO"
    else:
        return "YES"
