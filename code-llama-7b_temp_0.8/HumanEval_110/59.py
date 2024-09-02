
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

    even_numbers = [2, 4, 6, 8]
    # first check whether all elements in lst1 are even numbers
    if not lst1:
        return "YES"
    if all([elem in even_numbers for elem in lst1]):
        return "YES"

    # if lst1 has an odd number, and lst2 has an even number,
    # we can swap them and return "YES"
    if lst1 and not all([elem in even_numbers for elem in lst1]):
        if lst2 and all([elem in even_numbers for elem in lst2]):
            return "YES"

    return "NO"

