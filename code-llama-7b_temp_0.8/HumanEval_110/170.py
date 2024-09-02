
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
    # print(lst1, lst2)
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)
    if lst1[0] % 2 != 0:
        return "NO"

    for i, _ in enumerate(lst2):
        if lst1[0] == lst2[i]:
            lst2[i] = lst1[1]
            lst1[1] = lst2[i]
            lst1[0] = lst2[i]
            break
    # print(lst1, lst2)
    for i, _ in enumerate(lst2):
        if lst1[1] == lst2[i]:
            lst2[i] = lst1[2]
            lst1[2] = lst2[i]
            lst1[1] = lst2[i]
            break
    # print(lst1, lst2)
    for i, _ in enumerate(lst2):
        if lst1[2] == lst2[i]:
            lst2[i] = lst1[3]
            lst1[3] = lst2[i]
            lst1[2] = lst2[i]
            break
    if not any(i % 2 != 0 for i in lst1):
        return "YES"
    return "NO"

