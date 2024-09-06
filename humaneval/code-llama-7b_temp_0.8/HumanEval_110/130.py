
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

    even_count = 0
    odd_count = 0
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            odd_count += 1
        else:
            even_count += 1
    if odd_count == 0 or even_count == len(lst1):
        return "YES"
    for i in range(len(lst2)):
        if lst2[i] % 2 != 0:
            odd_count -= 1
        else:
            even_count -= 1
        if even_count == len(lst1) or odd_count == 0:
            return "YES"
    return "NO"

