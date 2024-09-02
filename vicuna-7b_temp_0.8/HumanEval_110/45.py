
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
    # base case
    if len(lst1) == 0 or len(lst2) == 0:
        return "YES" if len(lst1) == 0 else "NO"

    # find the largest number in lst1 and compare with the largest number in lst2
    largest1 = max(lst1)
    largest2 = max(lst2)

    # check if the largest numbers are the same
    if largest1 == largest2:
        # check if both lists have even number of elements
        if len(lst1) == len(lst2):
            return "YES"
        else:
            return "NO"

    # check if the largest number in lst1 is greater than the largest number in lst2
    if largest1 > largest2:
        # check if the elements in lst1 starting from the second element are all smaller than the elements in lst2
        smaller_lst = lst1[1:]
        if max(smaller_lst) < max(lst2[1:]):
            return "NO"

    # check if the largest number in lst1 is smaller than the largest number in lst2
    if largest1 < largest2:
        # check if the elements in lst2 starting from the second element are all smaller than the elements in lst1
        smaller_lst = lst2[1:]
        if max(smaller_lst) > max(lst1[1:]):
            return "NO"

    return "YES"