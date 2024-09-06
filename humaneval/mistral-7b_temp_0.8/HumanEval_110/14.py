
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
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    if lst1_len == 0 or lst2_len == 0:
        return "NO"
    for i in range(lst1_len):
        if lst1[i] % 2 == 0:
            lst1.remove(lst1[i])
    for i in range(lst2_len):
        if lst2[i] % 2 == 0:
            lst2.remove(lst2[i])
    for i in range(lst2_len):
        for j in range(lst1_len):
            if lst2[i] == lst1[j]:
                lst2.remove(lst2[i])
                lst1.remove(lst1[j])
                lst2.insert(i, lst1[j])
                lst1.insert(j, lst2[i])
                break
    if lst1_len == lst2_len and l
