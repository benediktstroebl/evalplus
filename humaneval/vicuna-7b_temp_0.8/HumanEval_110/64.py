
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
    n1 = len(lst1)
    n2 = len(lst2)
    if n1 != n2:
        return "NO"
    for i in range(n1):
        for j in range(n2):
            if lst1[i] != lst2[j]:
                return "NO"
        lst1[i] = lst2[i]
        for j in range(i+1, n1):
            if lst1[j] % 2 != 0:
                break
        else:
            lst2.append(lst1.pop(i))
    return "YES"
