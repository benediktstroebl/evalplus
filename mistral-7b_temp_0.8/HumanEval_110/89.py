
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
    list1 = lst1
    list2 = lst2
    count = 0
    for i in list1:
        if i % 2 == 0:
            count = count + 1
    if count != 0:
        for j in list2:
            if j % 2 != 0:
                for k in list1:
                    if k % 2 == 0:
                        list1[list1.index(k)] = j
                        list2[list2.index(j)] = k
        return "YES"
    else:
        return "NO"

