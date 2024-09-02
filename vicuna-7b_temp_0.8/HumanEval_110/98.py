
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
    # Check if all the elements of lst1 are odd
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            return "NO"
    # Check if all the elements of lst2 are odd
    for i in range(len(lst2)):
        if lst2[i] % 2 != 0:
            return "NO"
    # Check if it is possible to exchange elements between the lst1 and lst2
    # to make all the elements of lst1 to be even
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                lst1.remove(lst1[i])
                lst2.remove(lst2[j])
                for k in range(len(lst1)):
                    if k != i and k != j:
                        lst1[k] = lst1[i]
                        break
                else:
                    break
                for k in range(len(lst2)):
                    if k != i and k != j:
                        lst2[k] = lst2[j]
                        break
                else:
                    break
                if all(lst1_even) == True:
                    return "YES"
    return "NO"
