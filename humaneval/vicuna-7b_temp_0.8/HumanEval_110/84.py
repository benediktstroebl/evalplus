
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
    # Check if the input lists are empty
    if not lst1 and not lst2:
        return "YES"
    # Check if the last element of the first list is greater than the first element of the second list
    if lst1[-1] > lst2[0]:
        return "NO"
    # If not, check if all the elements of the first list are greater than or equal to the corresponding
    # elements of the second list
    for i in range(len(lst1)):
        if lst1[i] < lst2[i]:
            return "NO"
    return "YES"
