
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
    # Another solution - use set
    # return "YES" if len(set(lst1) - set(lst2)) == 0 else "NO"
    # return "YES" if len(set(lst1) - set(lst2)) == 0 or len(set(lst2) - set(lst1)) == 0 \
    #         else "NO"
    # Sol1 - list longer, use list comprehension
    lst1 = [i for i in lst1 if not i % 2]
    lst2 = [i for i in lst2 if not i % 2]
    if lst1 == lst2:
        return "YES"
    else:
        return "NO"
    # Sol2 - List shorter, use map
    # return "YES" if all(map(lambda x: x%2 == 0, lst1 + lst2)) else "NO"
    # return "YES" if all(map(lambda x: x%2 == 0, lst1 + lst2)) or all(map(lambda x: x%2 == 0, lst2 + lst1)) else "NO"

