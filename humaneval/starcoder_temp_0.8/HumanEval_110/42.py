
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
    if lst1 == lst2:
        return "NO"
    # Generate all possible swaps and count the number of even numbers.
    n_even = 0
    for i in range(len(lst1)):
        for j in range(i, len(lst1)):
            lst1[i], lst1[j] = lst1[j], lst1[i]
            if lst1[i] % 2 == 0 and lst1[j] % 2 == 0:
                n_even += 1
    return "YES" if n_even % 2 == 0 else "NO"
