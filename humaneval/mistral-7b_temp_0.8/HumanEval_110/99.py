
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
    even = [2, 4, 6, 8]
    list1 = lst1[:]
    list2 = lst2[:]
    j = 0
    k = 0
    while k < len(list1) and j < len(list2):
        if list1[k] not in even:
            list2.insert(j, list1[k])
            del list1[k]
            k -= 1
        k += 1
        j += 1
    if not list1:
        return "YES"
    else:
        return "NO"
