
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
    # Part 1: find out the different elements
    lst1_diff = []
    lst2_diff = []
    for item in lst1:
        if item % 2:
            lst1_diff.append(item)
    for item in lst2:
        if item % 2:
            lst2_diff.append(item)
    # Part 2: check if there are the same number of different elements in both lists
    if len(lst1_diff) == len(lst2_diff):
        # Part 3: make lst1 contains only even numbers
        for item in lst1_diff:
            if item in lst2_diff:
                # Part 4: find out the index of the item in lst2_diff
                # and remove that item from lst2_diff
                index = lst2_diff.index(item)
                lst2_diff.pop(index)
            else:
                return "NO"
        return "YES"
    else:
        return "NO"
