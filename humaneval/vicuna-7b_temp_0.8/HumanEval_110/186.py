
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
    # Check if lst1 and lst2 have the same number of elements
    if len(lst1) != len(lst2):
        return "NO"

    # Create a dictionary to store the elements of lst1
    lst1_dict = {}
    for num in lst1:
        lst1_dict[num] = 1

    # Create a dictionary to store the elements of lst2
    lst2_dict = {}
    for num in lst2:
        lst2_dict[num] = 1

    # Check if lst1 and lst2 are lists of only even numbers
    for num in lst1:
        if num % 2 != 0:
            return "NO"
    for num in lst2:
        if num % 2 != 0:
            return "NO"

    # Check if it is possible to perform an exchange of elements between lst1 and lst2
    # to make lst1 a list of only even numbers
    for num in lst1:
        # Check if the element can be exchanged with an element in lst2
        if num in lst2_dict and lst1_dict[num] == 1 and lst2_dict[lst2.index(num)+1] == 1:
            # Exchange the element with an element in lst2
            lst1.pop(lst1.index(num)+1)
            lst1.append(lst2.pop(lst2.index(num)+1))
            lst2.pop(lst2.index(num)+1)
            lst2.append(lst1.pop(lst1.index(num)+1))

    # Check if all the elements of lst1 are even
    for num in lst1:
        if num % 2 != 0:
            return "NO"

    return "YES"