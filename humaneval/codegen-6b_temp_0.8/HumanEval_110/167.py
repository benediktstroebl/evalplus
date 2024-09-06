
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
    # All the evens in the first list
    evens = [num for num in lst1 if num % 2 == 0]
    # All the evens in the second list
    evens_in_lst2 = [num for num in lst2 if num % 2 == 0]
    # Elements that we need to swap
    swap = [num for num in lst2 if num in evens]
    if len(swap) > len(evens_in_lst2):
        # We need to swap
        return "NO"
    else:
        # We don't need to swap
        # Removing the required elements from the lst2
        lst2 = [(num - num % 2) for num in lst2 if num % 2 != 0]
        if len(lst2) == 0:
            # All the elements are even, so the first list is a substitute for the second
            return "YES"
        else:
            # This part of the code is to be repeated until we've exhausted the lst1
            return exchange(lst1, lst2)

