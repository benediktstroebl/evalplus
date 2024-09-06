
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
    lst1 = lst1[:]
    lst2 = lst2[:]
    for e1 in lst1:
        for e2 in lst2:
            if e1 % 2 == 1 and e2 % 2 == 0:
                lst1.remove(e1)
                lst2.remove(e2)
                lst1 = lst1 + [e2] + [e1]
                lst2 = lst2 + [e1] + [e2]
                if len(lst1) == len(lst2):
                    return "YES"
    return "NO"

