
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

    count = 0
    # for x in range(len(lst1)):
    #     if lst1[x] % 2 != 0:
    #         for y in range(len(lst2)):
    #             if lst2[y] % 2 != 0:
    #                 if lst1[x] == lst2[y]:
    #                     count += 1
    #                     lst1.remove(lst1[x])
    #                     lst2.remove(lst2[y])
    #                     if count == len(lst1):
    #                         return "YES"
    #
    # return "NO"

    odd_list = []
    for x in range(len(lst1)):
        if lst1[x] % 2 != 0:
            odd_list.append(lst1[x])
            lst1.remove(lst1[x])
    for y in range(len(lst2)):
        if lst2[y] % 2 != 0:
            if lst2[y] in odd_list:
                odd_list.remove(lst2[y])
    if not odd_list:
        return "YES"
    return "NO"
