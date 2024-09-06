
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
    # print([x for x in lst1 if x % 2 != 0])
    if not [x for x in lst1 if x % 2 != 0]:
        return "YES"
    if not [x for x in lst2 if x % 2 != 0]:
        return "NO"

    lst1_even = []
    lst2_even = []
    for x in lst1:
        if x % 2 != 0:
            lst1_even.append(x)
    for x in lst2:
        if x % 2 != 0:
            lst2_even.append(x)

    # print(lst1_even, lst2_even)
    if not lst1_even:
        return "YES"
    elif not lst2_even:
        return "NO"
    else:
        lst1_even = sorted(lst1_even)
        lst2_even = sorted(lst2_even, reverse=True)
        # print(lst1_even, lst2_even)

        for i in range(len(lst1_even)):
            lst2_even[i] -= 1
        for i in range(len(lst1_even)):
            if lst1_even[i] != lst2_even[i]:
                return "NO"
        return "YES"

