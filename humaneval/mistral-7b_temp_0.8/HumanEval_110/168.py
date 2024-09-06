
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
    lst1.sort()
    lst2.sort()
    lst1_even = []
    lst2_odd = []
    for n in lst1:
        if n % 2 != 0:
            lst1_even.append(n)
    for n in lst2:
        if n % 2 != 0:
            lst2_odd.append(n)
    for n in lst1_even:
        if n in lst2_odd:
            lst1.remove(n)
            lst2.remove(n)
    if lst1_even:
        return 'NO'
    return 'YES'
