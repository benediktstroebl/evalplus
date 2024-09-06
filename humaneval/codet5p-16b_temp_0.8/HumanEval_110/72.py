
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

    lst1_even = []
    lst2_even = []
    lst1_odd = []
    lst2_odd = []

    for num in lst1:
        if num % 2 == 0:
            lst1_even.append(num)
        else:
            lst1_odd.append(num)

    for num in lst2:
        if num % 2 == 0:
            lst2_even.append(num)
        else:
            lst2_odd.append(num)

    if len(lst1_even) == len(lst1) and len(lst2_even) == len(lst2):
        return "YES"
    elif len(lst1_even) == len(lst1) and len(lst2_odd) == len(lst2):
        return "YES"
    elif len(lst1_odd) == len(lst1) and len(lst2_even) == len(lst2):
        return "YES"
    else:
        return
