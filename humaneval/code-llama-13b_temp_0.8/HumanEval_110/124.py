
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
    even_lst = []
    odd_lst = []
    if not isinstance(lst1, list):
        return 'Not list'
    elif not isinstance(lst2, list):
        return 'Not list'
    elif len(lst1) == 0 or len(lst2) == 0:
        return 'empty'
    else:
        for item in lst1:
            if item % 2 == 0:
                even_lst.append(item)
            else:
                odd_lst.append(item)
        if len(odd_lst) > len(even_lst):
            return 'NO'
        else:
            return 'YES'

