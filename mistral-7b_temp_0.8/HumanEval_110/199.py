
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
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    lst1_even = list(filter(lambda x: x % 2 == 0, lst1))
    if len(lst1_even) == len(lst1):
        return "YES"
    lst1_odd = list(filter(lambda x: x % 2 != 0, lst1))
    for element in lst1_odd:
        if element in lst2:
            lst1_odd.remove(element)
            lst2.remove(element)
            break
    lst2_even = list(filter(lambda x: x % 2 == 0, lst2))
    for element in lst2_even:
        if element in lst1:
            lst2_even.remove(element)
            lst1.remove(element)
            break
    if len(lst1_even) == len(lst1):
        return "YES"
    return "NO"

