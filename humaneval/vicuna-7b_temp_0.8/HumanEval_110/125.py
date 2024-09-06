
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
    # Iterate through the first list
    for i in range(len(lst1)):
        # If the current element is odd, append it to the second list
        if lst1[i] % 2 != 0:
            lst2.append(lst1[i])

    # Iterate through the second list
    for i in range(len(lst2)):
        # If the current element is odd, remove it from the second list
        if lst2[i] % 2 != 0:
            del lst2[i]

    # Return "YES" if all the elements of lst1 are even
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    else:
        return "NO"