
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
    even_lst1 = []
    even_lst2 = []
    odd_lst1 = []
    odd_lst2 = []
    for x in lst1:
        if x % 2 == 0:
            even_lst1.append(x)
        else:
            odd_lst1.append(x)
    for y in lst2:
        if y % 2 == 0:
            even_lst2.append(y)
        else:
            odd_lst2.append(y)
    # Check if lst1 has more even numbers than odd ones
    if len(even_lst1) > len(odd_lst1):
        return "NO"
    if len(odd_lst1) == 0:
        return "YES"
    # Check if odd_lst1 and odd_lst2 has the same number of elements
    if len(odd_lst1) == len(odd_lst2):
        # Check if there is an element that is present in odd_lst1 but not in odd_lst2
        for x in odd_lst1:
            if x not in odd_lst2:
                return "NO"
        return "YES"
    if len(odd_lst1) < len(odd_lst2):
        # Check if there is an element in odd_lst2 that is not in odd_lst1
        for y in odd_lst2:
            if y not in odd_lst1:
                return "NO"
    # Check if there is a pair of elements that matches in odd_lst1 and odd_lst2
    for x in odd_lst1:
        for y in odd_lst2:
            if x == y:
                return "YES"
    return "NO"
