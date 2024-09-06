
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
    # If lst1 and lst2 have the same length, then simply use this approach
    # to compute whether they can be exchanged.
    if len(lst1) != len(lst2):
        return "NO"

    # If lst1 and lst2 have the same number of even integers, then simply use this approach
    # to compute whether they can be exchanged.
    count1 = 0
    count2 = 0
    for i in lst1:
        if i % 2 == 0:
            count1 = count1 + 1
        else:
            pass
    for i in lst2:
        if i % 2 == 0:
            count2 = count2 + 1
        else:
            pass
    if count1 == count2:
        return "YES"

    # If lst1 and lst2 have the same number of even integers and
    # the number of uneven integers is less than the number of even integers,
    # then we can exchange the even integers first and the remaining
    # odd integers second.
    elif count1 != 0 and count2 != 0 and count1 < count2:
        i = 0
        j = 0
        while i < count1:
            if lst1[i] % 2 == 0:
                i = i + 1
            else:
                lst1[i], lst1[j] = lst1[j], lst1[i]
                i = i + 1
                j = j + 1
        while j < len(lst1):
            if lst1[j] % 2 != 0:
                lst1[j], lst1[-1] = lst1[-1], lst1[j]
                j = j + 1
                lst1[-1] = lst1[-1] - 1
            else:
                lst1[j], lst1[-1] = lst1[-1], lst1[j]
                j = j + 1
                lst1[-1] = lst1[-1] - 1

        return "YES"
    # If lst1 and lst2 have the same number of odd integers and
    # the