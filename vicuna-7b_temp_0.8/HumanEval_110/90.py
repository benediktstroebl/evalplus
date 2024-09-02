
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
    for i in range(n1):
        for j in range(n2):
            if lst1[i] > lst2[j]:
                exchanged = True
                for k in range(i):
                    if lst1[k] > lst2[j]:
                        exchanged = False
                        break
                for k in range(j):
                    if lst1[k] < lst2[i]:
                        exchanged = False
                        break
                if exchanged:
                    break
    return "YES" if (all(lst1[i] == 0 for i in range(n1)) or all(lst2[i] == 0 for i in range(n2))) else "NO"
