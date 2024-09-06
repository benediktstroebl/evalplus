
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
    if sum(lst1) % 2!= 0:
        return "NO"
    lst1.sort()
    lst2.sort()
    exchange_count = 0
    while lst1 and lst2:
        if lst1[-1] % 2 == 1:
            if lst2[-1] % 2 == 0:
                exchange_count += 1
                lst1.pop()
                lst2.pop()
            else:
                return "NO"
        else:
            lst1.pop()
            lst2.pop()
    while lst1 and lst1[-1] % 2!= 0:
        if lst2[-1] % 2!= 0:
            return "NO"
        lst1.pop()
        lst2.pop()
    return "YES" if lst1 == [] else "NO"

