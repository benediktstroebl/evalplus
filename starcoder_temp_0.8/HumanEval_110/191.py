
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
    def is_even(n):
        return n % 2 == 0

    def swap(x, y):
        return y, x

    def match_lists(lst1, lst2):
        if len(lst1) == len(lst2):
            for i in range(len(lst1)):
                if not (is_even(lst1[i]) and is_even(lst2[i])):
                    return False
            return True
        return False

    for x in lst1:
        for y in lst2:
            if match_lists(lst1, lst2):
                return "YES"
            else:
                lst1, lst2 = swap(lst1, lst2)

    return "NO"

