
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
    # Check for empty lists
    if not lst1 or not lst2:
        return "NO"
    
    # Check if the first element of lst1 is greater than the first element of lst2
    if lst1[0] > lst2[0]:
        return "NO"
    
    # Check if the first element of lst1 is equal to the first element of lst2
    if lst1[0] == lst2[0]:
        # Check if all elements of lst1 are greater than or equal to the first element of lst2
        for i in range(1, len(lst1)):
            if lst1[i] <= lst2[0]:
                return "NO"
    else:
        # Check if all elements of lst2 are greater than or equal to the first element of lst1
        for i in range(1, len(lst2)):
            if lst2[i] <= lst1[0]:
                return "NO"
    
    # Check if all elements of lst1 are even
    for i in range(1, len(lst1)):
        if not (lst1[i] % 2 == 0):
            return "NO"
    
    return "YES"