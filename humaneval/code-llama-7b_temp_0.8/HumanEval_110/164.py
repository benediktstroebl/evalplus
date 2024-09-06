
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
    if not lst1 or not lst2:
        raise ValueError('Input lists should not be empty.')
    if len(lst1) != len(lst2):
        raise ValueError('Both lists must be of same length.')
    if len(lst1) == 0:
        return 'YES'
    elif not [i for i in lst1 if i % 2 == 0]:
        return 'YES'
    if not [i for i in lst2 if i % 2 == 0]:
        return 'YES'
    if [i for i in lst1 if i % 2 != 0]:
        return 'NO'
    elif [i for i in lst2 if i % 2 != 0]:
        return 'NO'
    return 'YES'
