
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
    # you can use this condition to check if lst1 is a list of only odd numbers
    # and if lst2 is empty, then you can return "NO"
    # you can also check if the number of odd numbers in lst1 is equal to the number of even numbers in lst2
    # if either of the above conditions are not met, then you can return "NO"
    # but that would not be an efficient solution
    return "YES" if any(x % 2 == 0 for x in lst1) else "NO"