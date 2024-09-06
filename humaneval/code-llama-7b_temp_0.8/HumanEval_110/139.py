
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
        return "NO"
    if len(lst1) < len(lst2):
        lst2, lst1 = lst1, lst2
    # create list of odds
    odds = list(filter(lambda x: x % 2, lst2))
    # print(odds)
    # add even elements to lst1
    for even in filter(lambda x: x % 2 == 0, lst2):
        lst1.append(even)
    # print(lst1)
    if all(element % 2 == 0 for element in lst1):
        return "YES"
    else:
        return "NO"

