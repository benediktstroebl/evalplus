
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
    if len(lst1) != len(lst2):
        raise ValueError("Lists must be the same length.")

    if any(not isinstance(x, int) for x in lst1):
        raise TypeError("Lists must contain integers.")

    if any(not isinstance(x, int) for x in lst2):
        raise TypeError("Lists must contain integers.")

    if lst1 == lst2 or len(lst1) == 0:
        return "NO"

    def even_sum(lst):
        return sum(x for x in lst if x % 2 == 0)

    def odd_sum(lst):
        return sum(x for x in lst if x % 2 == 1)

    def swap(lst1, lst2):
        lst1_copy = lst1[:]
        lst2_copy = lst2[:]
        i = 0
        while odd_sum(lst1) < odd_sum(lst2) and i < len(lst1):
            if lst1[i] % 2 == 1:
                lst1_copy[i], lst2_copy[i] = lst2_copy[i], lst1_copy[i]
            i += 1
        return lst1_copy, lst2_copy

    lst1_copy, lst2_copy = swap(lst1, lst2)
    if even_sum(lst1_copy) == 0:
        return "YES"
    return "NO"
