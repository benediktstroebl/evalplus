
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

    # 1st solution
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]
    return "YES" if len(lst1_even) == len(lst1) + len(lst2_odd) else "NO"

    # 2nd solution
    lst1_even = []
    lst2_odd = []
    for i in lst1:
        if i % 2 == 0:
            lst1_even.append(i)
        else:
            lst2_odd.append(i)
    return "YES" if len(lst1_even) == len(lst1) + len(lst2_odd) else "NO"

    # 3rd solution
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]
    return "YES" if len(lst1_even) == len(lst1) + len(lst2_odd) else "NO"

    # 4th solution
    return "YES" if len([x for x in lst1 if x % 2 != 0]) == len(
        [x for x in lst2 if x % 2 == 0]) else "NO"
