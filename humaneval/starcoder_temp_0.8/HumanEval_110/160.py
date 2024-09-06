
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
    def check(lst, target):
        return all([e % 2 == 0 for e in lst])

    if check(lst1, 0) and check(lst2, 0):
        # If lst1 or lst2 already contain only even numbers, exchange is not necessary.
        return "YES"
    else:
        # Since exchange may create a list containing both odd and even numbers,
        # we need to check the case where all numbers in lst1 and lst2 are even or odd.
        return "YES" if check(lst1, 0) or check(lst2, 1) else "NO"
