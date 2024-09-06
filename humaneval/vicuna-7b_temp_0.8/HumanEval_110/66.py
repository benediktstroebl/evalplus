
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
    # Check if all elements of lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    # Check if all elements of lst2 are even
    if all(num % 2 == 0 for num in lst2):
        return "YES"
    # Check if all elements of lst1 are odd and all elements of lst2 are odd
    if all(num % 2 == 1 for num in lst1) and all(num % 2 == 1 for num in lst2):
        return "YES"
    # Check if all elements of lst1 are odd and some elements of lst2 are even
    if all(num % 2 == 1 for num in lst1) and any(num % 2 == 0 for num in lst2):
        return "NO"
    # Check if all elements of lst2 are odd and some elements of lst1 are even
    if all(num % 2 == 1 for num in lst2) and any(num % 2 == 0 for num in lst1):
        return "NO"
    # If none of the above conditions are met, return "NO"
    return "NO"