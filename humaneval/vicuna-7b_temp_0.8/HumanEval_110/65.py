
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
    # Check if the both lists are empty
    if not lst1 and not lst2:
        return "YES"

    # Check if lst1 contains only odd numbers and lst2 contains only even numbers
    if not any(lst1[1:] % 2 == 0 for lst1 in lst1):
        return "YES"

    # Check if it is possible to replace the odd numbers in lst1 with even numbers from lst2
    #
    # This check is done by checking if it is possible to remove all the odd numbers
    # from lst1 using only the even numbers from lst2
    even_count = sum(lst2 == 0 for lst2 in lst2)
    if even_count == len(lst2):
        return "YES"

    # If it is not possible to replace the odd numbers in lst1 with even numbers from lst2
    # then return "NO"
    return "NO"
