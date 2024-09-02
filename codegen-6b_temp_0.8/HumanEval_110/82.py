
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
    """
    Algorithm:
    1) create a new list with even elements of lst1
    2) extract matching elements from both lists to new lists
    3) if new lists are not the same, return "NO"
         otherwise return "YES"

    Complexity:
    Time: O(m+n)
    Space: O(m+n)
    """
    evens_1 = [e for e in lst1 if e % 2 == 0]
    evens_2 = [e for e in lst2 if e % 2 == 0]

    if evens_1 != evens_2:
        return "NO"


    for e1, e2 in zip(lst1, lst2):
        if e1 % 2 != 0 or e2 % 2 != 0:
            return "NO"

    return "YES"

