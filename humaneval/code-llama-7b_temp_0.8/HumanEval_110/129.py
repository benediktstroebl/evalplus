
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
    lst1 = sorted(lst1, reverse=True)
    lst2 = sorted(lst2)

    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[-1] == lst2[-1]:
            lst1.pop()
            lst2.pop()
        elif lst1[-1] % 2 == 0:
            lst1.pop()
        elif lst2[-1] % 2 == 0:
            lst2.pop()
        else:
            return "NO"

    return "YES"
