
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

    def add_list(lst, n):
        return lst + [n]

    def subtract_list(lst, n):
        return lst[1:]

    def is_even(n):
        return (n % 2) == 0

    lst1_is_even = True
    for n in lst1:
        lst1_is_even = lst1_is_even and is_even(n)

    lst2_is_even = True
    for n in lst2:
        lst2_is_even = lst2_is_even and is_even(n)

    if lst1_is_even:
        return "YES"

    if lst2_is_even:
        lst1, lst2 = lst2, lst1

    lst1_even = []
    lst1_odd = []
    for n in lst1:
        if is_even(n):
            lst1_even = add_list(lst1_even, n)
        else:
            lst1_odd = add_list(lst1_odd, n)

    lst2_even = []
    lst2_odd = []
    for n in lst2:
        if is_even(n):
            lst2_even = add_list(lst2_even, n)
        else:
            lst2_odd = add_list(lst2_odd, n)

    if lst1_odd == lst2_even:
        return "YES"

    if lst1_even == lst2_odd:
        return "YES"

    return "NO"

