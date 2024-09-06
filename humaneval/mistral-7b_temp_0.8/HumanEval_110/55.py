
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

    # get the length of lst1
    size_lst1 = len(lst1)

    # for each element in lst1
    for i in range(size_lst1):
        # check if the element is even
        if lst1[i] % 2 == 0:
            # check if the same element is present in lst2
            if lst2.count(lst1[i]) != 0:
                # replace the element in lst1 with an even element from lst2
                lst1[i] = lst2.pop(lst2.index(lst1[i]))

    # check if all elements in lst1 are even
    if not any(lst1):
        return "YES"
    else:
        return "NO"
