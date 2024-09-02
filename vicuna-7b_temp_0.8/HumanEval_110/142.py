
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
    # Check if there is no way to exchange elements
    if len(lst1) == len(lst2):
        return "NO"

    # Check the last element of lst1 and lst2
    if lst1[-1] != lst2[-1]:
        return "NO"

    # Check if all the elements in lst2 are less than lst1[-1]
    for i in range(len(lst2)):
        if lst2[i] >= lst1[-1]:
            return "NO"

    # Check if it is possible to exchange elements
    for i in range(len(lst1)-1):
        if lst1[i] > lst2[-1] and lst2[-1] != lst2[i]:
            exchanged = False
            for j in range(i+1, len(lst1)):
                if lst1[j] > lst2[-1] or (lst2[-1] == lst2[j] and lst1[j] > lst1[i]):
                    exchanged = True
                    break
            if not exchanged:
                return "YES"

    # If no exchange is possible, return "NO"
    return "NO"