
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
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    for i in lst1:
        if i % 2 == 1:
            return "NO"
    if len(lst1) == len(lst2):
        for i in lst2:
            for j in lst1:
                if i == j:
                    lst2.remove(i)
                    lst1.remove(j)
                    break
            if i in lst2 and j in lst1:
                lst2.remove(i)
                lst1.remove(j)
                break
        if len(lst1) == len(lst2):
            return "YES"
    else:
        return "NO"
