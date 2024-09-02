
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
    """
    # 1st solution
    # define two variables: even and odd
    # iterate lst1 and lst2
    # if element is even, add to even
    # else, add to odd
    # if even == odd, return yes, else return no
    # 2nd solution
    # sort lst1 and lst2
    # if first element is not even, return no
    # else, delete first element from both lists and check if
    # the other list is still sorted
    """
    # 1st solution
    if len(lst1) != len(lst2):
        return "NO"
    else:
        even = 0
        odd = 0
        lst1.sort()
        lst2.sort()
        for i in lst1:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        for i in lst2:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return "YES" if even == odd else "NO"
    """
    # 2nd solution
    lst1.sort()
    lst2.sort()
    if lst1[0] % 2 == 0:
        return "NO"
    else:
        lst1.pop(0)
        for i in lst1:
            if i % 2 != 0:
                lst2.pop(0)
                if len(lst2) > 0:
                    continue
                else:
                    return "NO"
        return "YES"
    """
    """leetcode solution"""
    lst1.sort()
    lst2.sort()
    value = len(lst1) - len(lst2)
    for i in range(0, len(lst1)):
        if lst1[i] % 2 != 0:
            value -= 1
        else:
            value += 1
    return "YES" if value == 0 else "NO"

assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert exchange([1, 2, 3, 4],